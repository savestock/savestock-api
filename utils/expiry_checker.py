from datetime import datetime

def check_expiry(expiry_date, days_threshold=7):
    try:
        expiry = datetime.strptime(expiry_date, '%Y-%m-%D')
        today = datetime.now()
        days_left = (expiry - today).days
        is_expired = days_left <= days_threshold
        return is_expired, days_left
    except ValueError:
        raise ValueError('Invalid date format. Use YYYY-MM-DD')
