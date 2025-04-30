# ExpiryGuard AI

This API lets you upload Excel/CSV files and automatically scans for products nearing expiry, sending WhatsApp and email alerts.

## Setup Instructions

1. Clone this repo.
2. Sign up at [vercel.com](https://vercel.com/), install Vercel CLI (`npm i -g vercel`).
3. Run `vercel deploy` in the project directory.
4. Add Environment Variables in Vercel dashboard:
   - `TWILIO_SID`
   - `TWILIO_TOKEN`
   - `TWILIO_WHATSAPP`
   - `SENDGRID_API_KEY`
   - `SENDER_EMAIL`
5. Test the API using Postman at `https://your-vercel-app.vercel.app/upload`.

## API Endpoints

- **POST /upload** - Upload an Excel/CSV file.
- **GET /test_apis** - Test WhatsApp and email APIs.

## Required Columns

- Product
- Batch
- Expiry_Date
- Stock
- Category
