from datetime import datetime, timedelta

def check_expiry_dates(data):
    warnings = []
    today = datetime.now().date()
    for item in data:
        try:
            expiry_date = datetime.strptime(item['Expiry_Date'], '%Y-%m-%d').date()
            days_left = (expiry_date - today).days

            if days_left <= 30:
                warning = f"⚠ {item['Product']} (Batch {item['Batch']}) expires in {days_left} days!"
                warnings.append(warning)
        except Exception as e:
            warnings.append(f"Error processing item {item.get('Product', 'Unknown')}: {str(e)}")

    return warnings
