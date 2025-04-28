import pandas as pd
import io
from datetime import datetime, timedelta

def process_stock_file(file_contents):
    df = pd.read_excel(io.BytesIO(file_contents))
    
    # Check for "expiry_date" and "price" columns
    if 'expiry_date' not in df.columns or 'price' not in df.columns:
        return {"error": "File must contain 'expiry_date' and 'price' columns."}
    
    now = datetime.now()
    soon_threshold = now + timedelta(days=30)  # 30 days from now

    discounted_prices = []
    
    for index, row in df.iterrows():
        expiry_str = str(row['expiry_date'])
        try:
            expiry_date = pd.to_datetime(expiry_str)
            price = row['price']
            if expiry_date <= soon_threshold:
                price = price * 0.8  # 20% discount
            discounted_prices.append(price)
        except Exception as e:
            discounted_prices.append(None)
    
    df['discounted_price'] = discounted_prices
    return df.to_dict(orient="records")
