from flask import Flask, request, jsonify
from utils.expiry_checker import process_file  # Import the process_file function

app = Flask(__name__)

# Route to upload file and check expiry dates
@app.route('/check_expiry', methods=['POST'])
def check_expiry_route():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Process the file and get the expiry check results
        result = process_file(file)
        
        # Return the processed results as JSON
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
    
