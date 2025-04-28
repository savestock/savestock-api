
# SaveStock API

This API lets you upload Excel/CSV files and automatically scans for products nearing expiry and sends WhatsApp alerts.

## Setup Instructions

1. Clone or upload this project to GitHub.
2. Create a free account at [Render.com](https://render.com).
3. Connect Render to your GitHub and deploy.
4. Add Environment Variables from `.env.example` (using real API keys).
5. Test your API using Postman.

## API Endpoints

- **POST /upload** - Upload an Excel or CSV file.

## Required Columns

- Product
- Batch
- Expiry_Date
- Stock

Enjoy automated expiry detection!
