#!/usr/bin/python

import Image
import ImageDraw
import ImageFont
import time
import json
import datetime
from rgbmatrix import Adafruit_RGBmatrix

# Generate png from string input
def generatetext(message, height):
    width = len(message)*17
    image = Image.new("RGBA", (width,height), (0,0,0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("subwayticker.ttf", height)
    draw.text((1, 0), message, (255,255,255), font=font)
    return image

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

# Display string message on LED matrix
def display(matrix, message, height):
    matrix.SetWriteCycles(4)
    matrix.Clear()
    fontsize = height/2
    image = generatetext(message, fontsize)
    drawheight = height - fontsize/2
    for n in range(32, -image.size[0], -1):
        matrix.SetImage(image.im.id, n, 8)
        time.sleep(0.025)
    matrix.Clear()
    #sys.exit()
    return

#matrix = Adafruit_RGBmatrix(32, 1)
#display(matrix, "Hello World1", 32)
#time.sleep(2)
#display(matrix, "Hello World2", 32)
#matrix.Clear()
