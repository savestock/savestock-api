import pandas as pd
from datetime import datetime, timedelta
import random

def load_stock_data(file_path):
    try:
        df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)
        required_columns = ['Product', 'Batch', 'Expiry_Date', 'Quantity', 'Category']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Excel must have Product, Batch, Expiry_Date, Quantity, and Category columns")
        df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])
        return df
    except Exception as e:
        return str(e)

def find_expiring_products(df, days=30):
    today = datetime.now()
    threshold = today + timedelta(days=days)
    expiring = df[df['Expiry_Date'] <= threshold]
    return expiring

def generate_discount_suggestions(expiring):
    suggestions = []
    for _, row in expiring.iterrows():
        discount = random.randint(20, 30)
        suggestion = f"Sell {row['Product']} (Category: {row['Category']}, Batch: {row['Batch']}) at {discount}% discount to clear {row['Quantity']} units before {row['Expiry_Date'].strftime('%Y-%m-%d')}"
        suggestions.append(suggestion)
    return suggestions

def generate_report(expiring, suggestions):
    if expiring.empty:
        return "No products expiring within 30 days."
    report = "ExpiryGuard AI Report\n\nExpiring Products:\n"
    for _, row in expiring.iterrows():
        report += f"- {row['Product']} (Category: {row['Category']}, Batch: {row['Batch']}): {row['Quantity']} units, expires {row['Expiry_Date'].strftime('%Y-%m-%d')}\n"
    report += "\nSuggestions:\n" + "\n".join(suggestions)
    return report
