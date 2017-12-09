from flask import Flask, request, render_template
import json
import matrix
app = Flask(__name__)

@app.route('/')
def index():
    messages = getRecentMessages(5)

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

    return render_template('welcome.html', message1=message1, message1timestamp=message1timestamp, message2=message2, message2timestamp=message2timestamp, message3=message3, message3timestamp=message3timestamp, message4=message4, message4timestamp=message4timestamp, message5=message5, message5timestamp=message5timestamp)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        #matrix.log(message)
        matrix.display(message, 32)
    return message

def getRecentMessages(number):
    log = json.load(open('log.json'))
    arrayOfMessageNames = list(map(int, log))
    mostRecentMessage = max(arrayOfMessageNames)
    result = []
    for i in range(mostRecentMessage-number+1, mostRecentMessage+1):
        result.append(log[str(i)])
    return result

if __name__ == '__main__':
   #app.run(debug = True)
   app.run(host='0.0.0.0')
