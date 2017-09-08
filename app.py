from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from tags import get_relevant_tags

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_reply():
    # Create MessagingResponse to generate TwiML
    resp = MessagingResponse()
    # If image is actually texted, then grab image
    if request.form['NumMedia'] != '0':
        image_url = request.form['MediaUrl0']
        relevant_tags = get_relevant_tags(image_url)
        resp.message('\n'.join(relevant_tags))
    else:
        resp.message('Send an image please')
    return str(resp)

if __name__ == '__main__':
    app.run()
