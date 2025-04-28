import pandas as pd
from datetime import datetime

# This function checks if the expiry date is in the past
def check_expiry(expiry_date_str):
    try:
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        return expiry_date < current_date
    except Exception as e:
        print(f"Error in check_expiry: {e}")
        return False

# This function processes the file and checks the expiry for each record
def process_file(file):
    try:
        # Read the uploaded file (assumes CSV for now)
        df = pd.read_csv(file)

        # Ensure that there is a column with expiry dates (e.g., 'expiry_date')
        if 'expiry_date' not in df.columns:
            return {"error": "No expiry_date column found in the file"}, 400

        # Check expiry for each row and add a new column 'is_expired' based on the result
        df['is_expired'] = df['expiry_date'].apply(check_expiry)

        # Convert the dataframe back to a dictionary for JSON response
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        return {"error": f"Error processing file: {str(e)}"}, 500
