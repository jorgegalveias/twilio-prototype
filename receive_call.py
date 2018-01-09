from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
  """Respond to incoming requests."""
  resp = VoiceResponse()
  resp.say("Hello Monkey")

  return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = '0.0.0.0'
    app.run(host=host,port=port,debug=True)

