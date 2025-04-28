
import os
from twilio.rest import Client

def send_whatsapp_alert(message):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_whatsapp_number = os.getenv('TWILIO_WHATSAPP_FROM')
    to_whatsapp_number = os.getenv('TWILIO_WHATSAPP_TO')
    if not all([account_sid, auth_token, from_whatsapp_number, to_whatsapp_number]):
        print("Twilio environment variables missing.")
        return
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=f'whatsapp:{from_whatsapp_number}',
        to=f'whatsapp:{to_whatsapp_number}'
    )
    print(f"Sent alert: {message.sid}")
