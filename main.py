#import files
from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse
from meli_bot import MeliBot

app = Flask(__name__)
bot = MeliBot()

@app.route("/bot", methods=['POST'])
def get_bot_response():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    response = bot.get_response(incoming_msg)
    if float(response.confidence) > 0.5:
      msg.body(response.text)
    else:
      msg.body('Desculpe, não entendi :(\n\n Voce pode repetir?')
    return str(resp)
if __name__ == "__main__":
    app.run()
