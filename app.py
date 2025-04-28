from flask import Flask, request, jsonify
from utils.expiry_checker import process_file

app = Flask(__name__)

@app.route('/check_expiry', methods=['POST'])
def check_expiry_route():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        result = process_file(file)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
