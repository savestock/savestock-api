from flask import Flask, request, jsonify
from utils.expiry_checker import process_file  # Import the process_file function

app = Flask(__name__)

# Route to upload file and check expiry dates
@app.route('/check_expiry', methods=['POST'])
def check_expiry_route():
    # Check if the file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    # Check if the file has a filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Process the file and get the expiry check results
        result = process_file(file)
        
        # If the result is a tuple (error message, status code), return that response
        if isinstance(result, tuple):
            return jsonify(result[0]), result[1]

        # Return the processed results as JSON
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
