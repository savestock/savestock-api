ExpiryGuard AI
This API lets you upload Excel/CSV files and automatically scans for products nearing expiry, sending WhatsApp and email alerts.
Setup Instructions

Clone this repo.
Sign up at vercel.com, install Vercel CLI (npm i -g vercel).
Run vercel deploy in the project directory.
Add Environment Variables in Vercel dashboard:
TWILIO_SID
TWILIO_TOKEN
TWILIO_WHATSAPP
SENDGRID_API_KEY
SENDER_EMAIL


Test the API using Postman at https://your-vercel-app.vercel.app/upload.

API Endpoints

POST /upload - Upload an Excel/CSV file.
GET /test_apis - Test WhatsApp and email APIs.

Required Columns

Product
Batch
Expiry_Date
Quantity
Category
