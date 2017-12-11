#!/usr/bin/env python
import time
import json
import datetime

from PIL import Image, ImageDraw, ImageFont

# Generate png from string input
def generatetext(message, height):
    width = int(len(message)*17)
    height = int(height)
    image = Image.new("RGBA", (width,height), (0,0,0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("subwayticker.ttf", height)
    draw.text((1, 0), message, (255,255,255), font=font)
    return image

# Display string message on LED matrix
def display(matrix, message, height):
    # Generate image from message
    fontsize = height/2
    image = generatetext(message, fontsize)
    # Draw image on screen
    for n in range(32, -image.size[0], -1):
        image = image.convert('RGB')
        matrix.SetImage(image, n, 8)
        time.sleep(0.025)
    del matrix
    return

#Log message to file
def log(message):
    #Generate timestamp
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%b %d, %Y %I:%M%p EST')
    #Open log from file
    with open("log.json") as logfile:
        log = json.load(logfile)
    #Add new message element to log dictionary
    arrayOfMessageNames = list(map(int, log))
    mostRecentMessage = max(arrayOfMessageNames)
    newMessage = mostRecentMessage + 1
    log[newMessage] = {"message":message, "timestamp":timestamp}
    #Write appended log back to file
    with open("log.json", 'w') as logfile:
        json.dump(log, logfile)
    return

#Grab a 'number' of most recent messages
def getRecentMessages(number):
    log = json.load(open('log.json'))
    arrayOfMessageNames = list(map(int, log))
    mostRecentMessage = max(arrayOfMessageNames)
    result = []
    for i in range(mostRecentMessage-number+1, mostRecentMessage+1):
        result.append(log[str(i)])
    return result
