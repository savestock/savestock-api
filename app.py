from flask import Flask, request, jsonify
import pandas as pd
from utils.expiry_checker import check_expiry_dates

app = Flask(__name__)

@app.route('/')
def home():
    return "SaveStock API is Live!"

@app.route('/upload_inventory', methods=['POST'])
def upload_inventory():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read Excel or CSV
        if file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
            df = pd.read_excel(file)
        elif file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            return jsonify({"error": "Unsupported file type"}), 400

        # Validate required columns
        required_columns = {'Product', 'Batch', 'Expiry_Date', 'Stock', 'Category'}
        if not required_columns.issubset(df.columns):
            return jsonify({"error": f"Missing columns. Required columns: {required_columns}"}), 400

        # Check expiry dates
        warnings = check_expiry_dates(df)

        return jsonify(warnings)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
