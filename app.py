from flask import Flask, request, jsonify
from utils.expiry_checker import check_expiry
from utils.whatsapp_alerts import send_whatsapp_alert

app = Flask(__name__)

@app.route('/')
def home():
    return "SaveStock API is running!"

@app.route('/check-expiry', methods=['POST'])
def check_expiry_route():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        result = check_expiry(file)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp_route():
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({"error": "Missing 'message' in request body"}), 400
        
        response = send_whatsapp_alert(data['message'])
        
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
