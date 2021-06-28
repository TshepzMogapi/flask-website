from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '../UPLOAD_FOLDER'

app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024

@app.route('/api/bot', methods=['POST'])
def bot():
    print('incoming_msg')
    incoming_msg = request.values.get('Body', '')
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    if 'Hi' in incoming_msg:
      msg.body('Hello I am going to help you today.')
    
    if 'Help' in incoming_msg:
      msg.body('I am getting you some help.')

    return  str(resp)

if __name__ == "__main__":
    app.run(debug=True)