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
