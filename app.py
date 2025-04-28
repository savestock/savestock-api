from flask import Flask, request, jsonify
import pandas as pd
from utils.whatsapp_alerts import send_whatsapp_alert
from utils.check_expiry import check_expiry_dates

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    if not {'Product', 'Batch', 'Expiry Date'}.issubset(df.columns):
        return jsonify({'error': 'Missing required columns'}), 400

    results = check_expiry_dates(df)
    for alert in results['alerts']:
        send_whatsapp_alert(alert)

    return jsonify(results), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the SaveStock API!"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
