
import pandas as pd
from datetime import datetime, timedelta

def check_expiry_dates(df):
    warnings = []
    today = datetime.today()
    for _, row in df.iterrows():
        try:
            expiry_date = pd.to_datetime(row['Expiry_Date'])
            days_left = (expiry_date - today).days
            if days_left < 30:
                discount = "10%" if row['Stock'] > 50 else "5%"
                warning = f"⚠ {row['Product']} (Batch {row['Batch']}) expires in {days_left} days! Suggest discount {discount}."
                warnings.append(warning)
        except Exception as e:
            continue
    return {
        "warnings": warnings,
        "total_flags": len(warnings)
    }
