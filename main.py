from flask import Flask, render_template
import matrix
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/send/<message>')
def submit(message):
    matrix.text(message)
    return message

if __name__ == '__main__':
   app.run(debug = True)
