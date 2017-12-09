#!/usr/bin/env python
import time
import json
import datetime
from rgbmatrix import RGBMatrix, RGBMatrixOptions
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

#Log message to file
def log(message):
    #Generate timestamp
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%b %d, %Y %I:%M%p EST')
    #Remove newline from message
    "".join(message.splitlines())
    #Create new entry
    newentry = timestamp +"~~~$~~~"+ message
    #Open log from file
    with open("log.txt", "a") as logfile:
        #Write appended log back to file
        logfile.write(newentry)
        #Close logfile
        logfile.close()
    return

# Display string message on LED matrix
def display(message, height):
    # Generate image from message
    fontsize = height/2
    image = generatetext(message, fontsize)
    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
    # Create RGBMatrix object with specified options
    matrix = RGBMatrix(options = options)
    # Draw image on screen
    for n in range(32, -image.size[0], -1):
        image = image.convert('RGB')
        matrix.SetImage(image, n, 8)
        time.sleep(0.025)
    return
