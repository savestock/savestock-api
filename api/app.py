from flask import Flask, request, jsonify
from utils.expiry_checker import load_stock_data, find_expiring_products, generate_discount_suggestions, generate_report
from utils.whatsapp_alerts import send_whatsapp_alert, send_email_alert
import os

app = Flask(__name__)

# Environment variables (set in Vercel dashboard)
TWILIO_SID = os.getenv("TWILIO_SID", "YOUR_TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN", "YOUR_TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP", "whatsapp:+14155238886")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "YOUR_SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your@gmail.com")

@app.route('/upload', methods=['POST'])
def process_stock():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files['file']
        file_path = f"/tmp/{file.filename}"  # Vercel uses /tmp for file storage
        file.save(file_path)
        
        df = load_stock_data(file_path)
        if isinstance(df, str):
            return jsonify({"error": df}), 400
        
        expiring = find_expiring_products(df)
        suggestions = generate_discount_suggestions(expiring)
        report = generate_report(expiring, suggestions)
        
        send_whatsapp_alert(report, TWILIO_SID, TWILIO_TOKEN, TWILIO_WHATSAPP, "whatsapp:+923001234567")
        send_email_alert(report, SENDGRID_API_KEY, SENDER_EMAIL, "client@example.com")
        
        return jsonify({"report": report})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/test_apis', methods=['GET'])
def test_apis():
    try:
        test_message = "Test from ExpiryGuard AI"
        whatsapp_result = send_whatsapp_alert(test_message, TWILIO_SID, TWILIO_TOKEN, TWILIO_WHATSAPP, "whatsapp:+923001234567")
        email_result = send_email_alert(test_message, SENDGRID_API_KEY, SENDER_EMAIL, "your@gmail.com")
        return jsonify({"status": "APIs working", "whatsapp": whatsapp_result, "email": email_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel serverless function entry point
def handler(request):
    return app(request.environ, start_response)
