from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO SID HERE"
TWILIO_AUTH_TOKEN = "YOUR TWILIO TOKEN HERE"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER HERE"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER HERE"


class NotificationManager:
    """
    Access twilio API to send custom sms
    """
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)