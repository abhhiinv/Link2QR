# Link2QR

A Django web app that converts text or URLs into downloadable QR codes and barcodes instantly in the browser.

🔗 **Live Demo:** https://link2qr-scqm.onrender.com/

---

## Features

- Generate a QR code from any text or URL
- Generate a barcode from any text or URL
- Download QR codes as PNG files
- Download barcodes as PNG files
- Tabbed interface to switch between QR and barcode sections
- Instant generation on form submit

---

## Tech Stack

- Python / Django
- qrcode
- python-barcode
- Pillow
- Gunicorn
- Whitenoise
- python-dotenv

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Clone and Run Locally

```bash
git clone https://github.com/abhhiinv/link2qr.git
cd link2qr
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

Run the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

---

## Deployment

Deployed on [Render](https://render.com) using Gunicorn as the WSGI server and Whitenoise for static file serving.