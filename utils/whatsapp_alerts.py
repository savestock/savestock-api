from twilio.rest import Client
import os

def send_whatsapp(to_number, message):
    try:
        client = Client(os.environ.get('TWILIO_SID'), os.environ.get('TWILIO_TOKEN'))
        message = client.messages.create(
            from_=os.environ.get('TWILIO_WHATSAPP'),
            body=message,
            to=f'whatsapp:{to_number}'
        )
        return message.sid
    except Exception as e:
        raise Exception(f'WhatsApp send failed: {str(e)}')
