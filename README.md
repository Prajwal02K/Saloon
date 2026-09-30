# 7 Start Salon — Hair Salon

Mobile-first salon site built with Flask and Firebase Firestore, with automatic
local JSON demo mode until a Firebase service key is configured.

## Features
- `/` — salon home and location
- `/services` — admin-managed services and INR prices
- `/gallery` — admin-managed salon photos
- `/booking` — four-step service, stylist, date, and time booking
- `/reviews` — customer reviews
- `/admin` — sign in, manage bookings/services/gallery, and add admin accounts
- Photos are uploaded as JPG, PNG, or WebP files up to 8 MB.

## Code layout
- `app.py` creates the Flask app and registers route blueprints.
- `routes/pages.py` serves customer and admin pages.
- `routes/public_api.py` handles public booking availability, bookings, and reviews.
- `routes/admin_auth.py` handles admin login, first-account setup, and logout.
- `routes/admin_catalog.py` handles services, salon settings, and gallery uploads.
- `routes/admin_bookings.py` handles appointment management.
- `db.py` selects Firestore or local demo storage; operational salon content is stored there.

## Run it
```bash
cd hair-salon
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # set app secrets and Firebase options
python app.py
```
Site → http://127.0.0.1:5000 · Admin → http://127.0.0.1:5000/admin

Before the first admin signup, set `FLASK_SECRET_KEY` and `ADMIN_SETUP_KEY` to
private random values in `.env`. Use the setup key once on `/admin/signup` to
create the first username/password. Public signup then closes; signed-in admins
can create additional admin accounts from the dashboard.

To enable Firestore, revoke any service-account key that has been shared or
committed, create a replacement in Firebase Console, and store the new JSON
outside source control. Set `FIREBASE_CREDENTIALS` in `.env` to its path. The key file is
git-ignored. Services, gallery photos, stylists, and business hours are stored
in the database and are not populated with sample records on startup. Add the
salon name, currency, contact details, services, stylists, business hours, and
photos through the Admin dashboard; existing records are preserved.

Enable Firebase Storage and set `FIREBASE_STORAGE_BUCKET` to its bucket name to
store Admin-uploaded gallery images in the cloud. Without a bucket, Firestore
mode keeps uploads disabled with a setup message; local demo mode stores uploads
under the ignored `static/images/uploads/` directory.

## Go live with Firebase
1. Firebase Console → create project → **Firestore Database** → Start in test mode
2. Project settings → Service accounts → **Generate new private key**
3. Save it outside source control and set its path as `FIREBASE_CREDENTIALS` in `.env`
4. Restart the app — done. 🔥 (Reviews & bookings now persist in the cloud.)

## Deploy (optional)
```bash
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```
