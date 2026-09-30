# 7 Star Salon

A full-stack salon booking website built with **Flask** and **Firebase Firestore**.
Customers can browse services, view the gallery, book appointments, and leave reviews — all from any device. The owner manages everything through a private admin dashboard.

Live demo: *coming soon after deployment*

---

## Features

| Area | What it does |
|---|---|
| Home | Salon info, opening hours, WhatsApp link, Google Maps |
| Services | Full service menu with prices and durations |
| Gallery | Salon photo gallery managed by the owner |
| Booking | 3-step appointment booking (service → date/time → details) |
| Reviews | Customers can read and submit reviews |
| Admin | Owner dashboard — manage bookings, services, gallery, settings |

---

## Tech Stack

- **Backend** — Python / Flask
- **Database** — Firebase Firestore
- **Storage** — Firebase Storage (gallery photos)
- **Auth** — Session-based admin login (bcrypt password hashing)
- **Frontend** — Vanilla JS, CSS (no frameworks)
- **Deployment** — Render (free tier)

---

## Project Structure

```
hair-salon/
├── app.py                 # Flask app entry point
├── db.py                  # All Firebase read/write operations
├── config.py              # Environment variable loader
├── requirements.txt       # Python dependencies
├── Procfile               # Render/gunicorn start command
├── render.yaml            # Render deployment config
├── routes/
│   ├── pages.py           # Customer-facing pages
│   ├── public_api.py      # Booking and review APIs
│   ├── admin_auth.py      # Admin login / signup
│   ├── admin_bookings.py  # Booking management API
│   └── admin_catalog.py   # Services, gallery, settings API
├── templates/             # Jinja2 HTML templates
└── static/                # CSS, JS, images
```

---

## Local Development

**1. Clone and set up**
```bash
git clone https://github.com/Prajwal02K/Saloon.git
cd Saloon
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

**2. Configure environment**
```bash
cp .env.example .env
```
Edit `.env` and fill in:
- `FLASK_SECRET_KEY` — any long random string
- `ADMIN_SETUP_KEY` — used once to create first admin account
- `FIREBASE_CREDENTIALS` — path to your Firebase service account JSON
- `FIREBASE_STORAGE_BUCKET` — your Firebase Storage bucket name
- `SALON_NAME`, `WHATSAPP_NUMBER`, `MAPS_QUERY` — your salon details

**3. Run**
```bash
python app.py
```
Site → http://127.0.0.1:5000

---

## First-time Admin Setup

1. Go to `http://127.0.0.1:5000/admin/signup`
2. Enter a username, password (10+ chars), and your `ADMIN_SETUP_KEY`
3. Log in at `/admin/login`
4. Go to **Settings** → add your stylist and opening hours → Save
5. Go to **Services** → add your services

---

## Deploy to Render

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service → connect repo
3. Render auto-reads `render.yaml`
4. In the Render dashboard → **Environment** tab, add these secrets manually:

| Key | Value |
|---|---|
| `ADMIN_SETUP_KEY` | your chosen setup password |
| `FLASK_SECRET_KEY` | click Generate |
| `FIREBASE_CREDENTIALS_JSON` | paste entire contents of `serviceAccountKey.json` |

5. Click **Deploy** — your site goes live at `https://7-star-salon.onrender.com`

---

## Firebase Collections

| Collection | Purpose |
|---|---|
| `settings / public` | Salon name, hours, stylists, WhatsApp |
| `services` | Service menu (name, price, duration) |
| `bookings` | Customer appointments |
| `reviews` | Customer reviews |
| `gallery` | Gallery photo records |
| `admins` | Admin accounts |

---

## Environment Variables

| Variable | Purpose |
|---|---|
| `FLASK_SECRET_KEY` | Secures user sessions |
| `ADMIN_SETUP_KEY` | One-time key to create first admin |
| `FIREBASE_CREDENTIALS` | Path to service-account JSON (local) |
| `FIREBASE_CREDENTIALS_JSON` | Full JSON string (cloud/Render) |
| `FIREBASE_STORAGE_BUCKET` | Firebase Storage bucket name |
| `SALON_NAME` | Your salon name |
| `CURRENCY_SYMBOL` | Currency symbol (e.g. Rs) |
| `WHATSAPP_NUMBER` | WhatsApp number with country code |
| `MAPS_QUERY` | Address for Google Maps link |

---

Built for **7 Star Salon** — Lingegowdanadoddi, Owner.
