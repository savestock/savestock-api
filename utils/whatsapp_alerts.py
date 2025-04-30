from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_whatsapp_alert(report, twilio_sid, twilio_token, twilio_whatsapp, to_number):
    try:
        client = Client(twilio_sid, twilio_token)
        message = client.messages.create(
            body=report,
            from_=twilio_whatsapp,
            to=to_number
        )
        return f"WhatsApp alert sent, SID: {message.sid}"
    except Exception as e:
        return str(e)

def send_email_alert(report, sendgrid_api_key, sender_email, to_email):
    try:
        message = Mail(
            from_email=sender_email,
            to_emails=to_email,
            subject="ExpiryGuard AI Report",
            plain_text_content=report)
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        return f"Email sent, status: {response.status_code}"
    except Exception as e:
        return str(e)
