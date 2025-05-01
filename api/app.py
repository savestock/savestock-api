from flask import Flask, request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
import os
from utils.expiry_checker import check_expiry
from utils.whatsapp_alerts import send_whatsapp

app = Flask(__name__)

@app.route('/test_apis', methods=['GET'])
def test_api():
    try:
        # Test SendGrid email
        message = Mail(
            from_email=os.environ.get('SENDER_EMAIL'),
            to_emails='recipient@example.com',  # Replace with test email
            subject='ExpiryGuard Test',
            html_content='<strong>Hello from ExpiryGuard!</strong>')
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        email_response = sg.send(message)

        # Test Twilio WhatsApp
        whatsapp_response = send_whatsapp(
            to_number='+1234567890',  # Replace with test number
            message='Hello from ExpiryGuard!'
        )

        return jsonify({
            'status': 'success',
            'email_status': email_response.status_code,
            'whatsapp_sid': whatsapp_response
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/check_expiry', methods=['POST'])
def check_expiry_endpoint():
    try:
        data = request.get_json()
        item_name = data.get('item_name')
        expiry_date = data.get('expiry_date')  # Format: YYYY-MM-DD
        days_threshold = data.get('days_threshold', 7)

        if not item_name or not expiry_date:
            return jsonify({'status': 'error', 'message': 'Missing item_name or expiry_date'}), 400

        is_expired, days_left = check_expiry(expiry_date, days_threshold)

        if is_expired:
            # Send email alert
            message = Mail(
                from_email=os.environ.get('SENDER_EMAIL'),
                to_emails='recipient@example.com',  # Replace with user email
                subject=f'Expiry Alert: {item_name}',
                html_content=f'<strong>{item_name} expires in {days_left} days!</strong>')
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(message)

            # Send WhatsApp alert
            send_whatsapp(
                to_number='+1234567890',  # Replace with user number
                message=f'{item_name} expires in {days_left} days!'
            )

        return jsonify({
            'status': 'success',
            'item_name': item_name,
            'is_expired': is_expired,
            'days_left': days_left
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run()
