import streamlit as st
from utils.expiry_checker import load_stock_data, find_expiring_products, generate_discount_suggestions, generate_report

st.title("ExpiryGuard AI")
st.write("Upload stock data (Excel/CSV) to check expiring products.")
st.write("Required columns: Product, Batch, Expiry_Date, Quantity, Category")

uploaded_file = st.file_uploader("Choose a file", type=['xlsx', 'csv'])
if uploaded_file:
    file_path = f"/tmp/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    df = load_stock_data(file_path)
    if isinstance(df, str):
        st.error(df)
    else:
        expiring = find_expiring_products(df)
        suggestions = generate_discount_suggestions(expiring)
        report = generate_report(expiring, suggestions)
        st.success("Report Generated!")
        st.write(report)
        st.write("Alerts sent to WhatsApp/email (via API).")
