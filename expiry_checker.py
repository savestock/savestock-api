from datetime import datetime, timedelta

def check_expiry_dates(df):
    warnings = []
    today = datetime.today()
    discount_items = []

    # Loop through each item in the inventory
    for index, row in df.iterrows():
        try:
            expiry_date = datetime.strptime(str(row['Expiry_Date']), '%Y-%m-%d')
            days_to_expiry = (expiry_date - today).days

            if days_to_expiry <= 30:
                warning_message = f"⚠ {row['Product']} (Batch {row['Batch']}) expires in {days_to_expiry} days. Apply 20% discount."
                warnings.append(warning_message)

                discount_items.append({
                    "product": row['Product'],
                    "batch": row['Batch'],
                    "category": row['Category'],
                    "stock": row['Stock'],
                    "days_to_expiry": days_to_expiry,
                    "recommended_discount": "20%"
                })

        except Exception as e:
            warnings.append(f"Error processing row {index + 1}: {str(e)}")

    return {
        "warnings": warnings,
        "discount_recommendations": discount_items
    }
