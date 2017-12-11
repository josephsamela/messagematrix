from flask import Flask, request, render_template
import json
import matrix
from rgbmatrix import RGBMatrix, RGBMatrixOptions
app = Flask(__name__)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
# Create RGBMatrix object with specified options
m = RGBMatrix(options = options)

@app.route('/')
def index():
    # Grab the 5 most recent messages
    messages = matrix.getRecentMessages(5)
    # Structure recent message variables
    message1 = messages[4]["message"]
    message1timestamp = messages[4]["timestamp"]
    message2 = messages[3]["message"]
    message2timestamp = messages[3]["timestamp"]
    message3 = messages[2]["message"]
    message3timestamp = messages[2]["timestamp"]
    message4 = messages[1]["message"]
    message4timestamp = messages[1]["timestamp"]
    message5 = messages[0]["message"]
    message5timestamp = messages[0]["timestamp"]
    #return render_template('welcome.html')
    return render_template('welcome.html', message1=message1, message1timestamp=message1timestamp, message2=message2, message2timestamp=message2timestamp, message3=message3, message3timestamp=message3timestamp, message4=message4, message4timestamp=message4timestamp, message5=message5, message5timestamp=message5timestamp)

@app.route('/post', methods=['POST'])
def display():
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        matrix.log(message)
        matrix.display(m, message, 32)
    return message

if __name__ == '__main__':
   #app.run(debug = True)
   app.run(host='0.0.0.0')
