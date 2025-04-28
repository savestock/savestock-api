import pandas as pd
from datetime import datetime, timedelta

def check_expiry_dates(file_path):
    df = pd.read_excel(file_path)

    today = datetime.today()
    near_expiry_threshold = today + timedelta(days=30)

    expired_products = []
    near_expiry_products = []
    offer_products = []

    for _, row in df.iterrows():
        expiry_date = row['Expiry_date']

        if pd.isna(expiry_date):
            continue

        if isinstance(expiry_date, str):
            expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")

        if expiry_date < today:
            expired_products.append({
                "product": row['product'],
                "batch": row['batch'],
                "expiry_date": expiry_date.strftime("%Y-%m-%d"),
                "stock": row['stock'],
                "category": row['category']
            })
        elif today <= expiry_date <= near_expiry_threshold:
            near_expiry_products.append({
                "product": row['product'],
                "batch": row['batch'],
                "expiry_date": expiry_date.strftime("%Y-%m-%d"),
                "stock": row['stock'],
                "category": row['category']
            })
            offer_products.append({
                "product": row['product'],
                "batch": row['batch'],
                "expiry_date": expiry_date.strftime("%Y-%m-%d"),
                "stock": row['stock'],
                "category": row['category'],
                "offer": "Sell at 20% discount"
            })

    return expired_products, near_expiry_products, offer_products
