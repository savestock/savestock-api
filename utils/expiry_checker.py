# utils/expiry_checker.py

from datetime import datetime

def check_expiry(expiry_date_str, date_format="%Y-%m-%d"):
    """
    Check if a given expiry date (in string format) has passed.

    Args:
        expiry_date_str (str): Expiry date as a string (e.g., '2025-04-28').
        date_format (str): Format of the expiry date string.

    Returns:
        bool: True if expired, False otherwise.
    """
    try:
        expiry_date = datetime.strptime(expiry_date_str, date_format)
        return datetime.now() > expiry_date
    except Exception as e:
        print(f"Error checking expiry: {e}")
        return False
