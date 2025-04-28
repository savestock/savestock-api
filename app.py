from flask import Flask, request, jsonify
import pandas as pd
from utils.expiry_checker import check_expiry_dates

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to SaveStock API!"

@app.route('/upload', methods=['POST'])
def upload_inventory():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return jsonify({'error': 'Unsupported file format'}), 400

        # Validate required columns
        required_columns = {'Product', 'Batch', 'Expiry_Date', 'Stock', 'Category'}
        if not required_columns.issubset(set(df.columns)):
            return jsonify({'error': f'Missing required columns: {required_columns - set(df.columns)}'}), 400

        # Process expiry checking
        result = check_expiry_dates(df)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
