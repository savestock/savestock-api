import pandas as pd
from datetime import datetime
import io

def check_expiry(expiry_date_str):
    try:
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
        return expiry_date < datetime.now()
    except Exception as e:
        print(f"Error parsing expiry date: {e}")
        return False

def process_file(file):
    try:
        # Read file bytes
        content = file.read()

        # Try to decode with utf-8 first
        try:
            decoded = content.decode('utf-8')
        except UnicodeDecodeError:
            decoded = content.decode('ISO-8859-1')

        # Now create a StringIO object
        data = io.StringIO(decoded)

        # Now read CSV
        df = pd.read_csv(data)

        if 'expiry_date' not in df.columns:
            return {"error": "No 'expiry_date' column found in the file"}

        df['is_expired'] = df['expiry_date'].apply(check_expiry)

        return df.to_dict(orient='records')

    except Exception as e:
        return {"error": f"Error processing file: {str(e)}"}
