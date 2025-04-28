import datetime
import pandas as pd

def check_expiry_dates(df):
    warnings = []
    today = datetime.datetime.now().date()

    for index, row in df.iterrows():
        try:
            expiry_date = pd.to_datetime(row['Expiry_Date']).date()
            days_left = (expiry_date - today).days
            stock = int(row['Stock'])
            product = row['Product']
            batch = row['Batch']
            category = row['Category']

            if days_left < 0:
                warnings.append({
                    "product": product,
                    "batch": batch,
                    "category": category,
                    "status": "Expired",
                    "message": f"❌ {product} (Batch {batch}) already expired!",
                    "suggestion": "Remove from shelves immediately."
                })
            elif days_left <= 30:
                discount = 20  # Always 20% for nearly expired products
                warnings.append({
                    "product": product,
                    "batch": batch,
                    "category": category,
                    "status": "Expiring Soon",
                    "message": f"⚠️ {product} (Batch {batch}) expires in {days_left} days.",
                    "suggestion": f"Offer {discount}% discount to boost sales immediately."
                })

        except Exception as e:
            warnings.append({
                "error": f"Error processing row {index}: {str(e)}"
            })

    if not warnings:
        return {"message": "✅ No products nearing expiry!"}

    return {"warnings": warnings}
