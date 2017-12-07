from flask import Flask, render_template
import matrix
import threading
from rgbmatrix import Adafruit_RGBmatrix
app = Flask(__name__)

m = Adafruit_RGBmatrix(32, 1)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/send/<message>')
def submit(message):
    matrix.log(message)
    matrix.display(m, message, 32)
    return message

if __name__ == '__main__':
   #app.run(debug = True)
   app.run(host='0.0.0.0')
