# WeTravel — Backend

Django 5 + Django REST Framework API for WeTravel, a safety and welcome guide for Black travelers, African diaspora, and mixed-race couples.

---

## Stack

| Layer | Technology |
|---|---|
| Framework | Django 5 + Django REST Framework |
| Auth | `djangorestframework-simplejwt` + `dj-rest-auth` + `django-allauth` (Google OAuth2) |
| Database | PostgreSQL 16 |
| Cache / Broker | Redis 7 |
| Task queue | Celery + Redis |
| Storage | AWS S3 / Cloudflare R2 (optional) |
| API docs | drf-spectacular (OpenAPI 3) |
| Error tracking | GlitchTip (Sentry-compatible) |
| Analytics | Matomo |
| Server | Gunicorn |

---

## Services & Ports

| Service | URL | Notes |
|---|---|---|
| **Django API** | http://localhost:8000 | REST API + admin |
| **Django Admin** | http://localhost:8000/admin/ | Superuser required |
| **API Docs (Swagger)** | http://localhost:8000/api/schema/swagger-ui/ | Auto-generated from DRF |
| **API Docs (ReDoc)** | http://localhost:8000/api/schema/redoc/ | |
| **PostgreSQL** | localhost:5432 | DB: `wetravel`, User: `wetravel` |
| **Redis** | localhost:6379 | Shared by Django cache and Celery |
| **GlitchTip** | http://localhost:8090 | Error tracking (Sentry-compatible) |
| **Matomo** | http://localhost:8080 | Web analytics |

---

## Quick Start (Docker — recommended)

### 1. Clone & configure

```bash
git clone <repo-url>
cd wetravel-back
cp .env.example .env   # then edit .env with your values
```

### 2. Start all services

```bash
docker compose up -d
```

This starts: PostgreSQL, Redis, Django backend, Matomo, Matomo DB, GlitchTip (web + worker).  
Migrations run automatically on backend startup.

### 3. Create a Django superuser

```bash
docker compose exec backend python manage.py createsuperuser
```

### 4. Seed the database

```bash
# Seed cities (runs the data migration — already included in normal migrate)
docker compose exec backend python manage.py migrate

# Fetch place data from Google Places API (requires GOOGLE_PLACES_API_KEY)
docker compose exec backend python manage.py fetch_places

# Fetch hero images from Unsplash (requires UNSPLASH_ACCESS_KEY)
docker compose exec backend python manage.py fetch_city_images

# Force re-fetch hero images even if already set
docker compose exec backend python manage.py fetch_city_images --force

# Dry run (logs what would be fetched without saving)
docker compose exec backend python manage.py fetch_city_images --dry-run
```

### 5. Verify

```bash
curl http://localhost:8000/api/cities/
```

---

## Quick Start (local — without Docker)

```bash
# Python environment
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Environment
cp .env.example .env   # edit .env

# Requires local PostgreSQL and Redis running
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Optional: Celery worker (separate terminal)
celery -A wetravel_back worker -l info

# Optional: Celery beat scheduler (separate terminal)
celery -A wetravel_back beat -l info
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in the values.

```env
# Django
SECRET_KEY=                        # required — generate with: python -c "import secrets; print(secrets.token_urlsafe(50))"
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173

# Database
DATABASE_URL=postgres://wetravel:wetravel@db:5432/wetravel
POSTGRES_DB=wetravel
POSTGRES_USER=wetravel
POSTGRES_PASSWORD=wetravel
POSTGRES_PORT=5432

# Redis
REDIS_URL=redis://redis:6379/0

# Google OAuth2
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

# External APIs
GOOGLE_PLACES_API_KEY=             # for fetch_places management command
UNSPLASH_ACCESS_KEY=               # for fetch_city_images management command
BOOKING_AFFILIATE_ID=              # Booking.com affiliate ID

# AWS / Cloudflare R2 (optional — leave blank to use local storage)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=

# GlitchTip error tracking
GLITCHTIP_PORT=8090
GLITCHTIP_DB_PASSWORD=             # choose a strong password
GLITCHTIP_SECRET_KEY=              # choose a long random string
SENTRY_DSN=                        # paste from GlitchTip after creating a project

# Matomo analytics
MATOMO_PORT=8080
MYSQL_ROOT_PASSWORD=
MYSQL_DATABASE=matomo
MYSQL_USER=matomo
MYSQL_PASSWORD=
MATOMO_DATABASE_HOST=matomo-db
MATOMO_DATABASE_ADAPTER=mysql
MATOMO_DATABASE_TABLES_PREFIX=matomo_

# Backend port
BACKEND_PORT=8000
```

---

## GlitchTip — Error Tracking

GlitchTip is a self-hosted, Sentry-compatible error tracker. It captures Python exceptions, performance transactions, and logs from the Django backend.

### First-time setup

1. Open http://localhost:8090
2. Create an account (first registration becomes the admin)
3. Create an **Organization** (e.g. `wetravel`)
4. Create a **Project** → choose **Django** → name it `wetravel-back`
5. Copy the generated **DSN** — it looks like:
   ```
   http://<key>@localhost:8090/<project-id>
   ```
6. In your `.env`, set:
   ```env
   SENTRY_DSN=http://<key>@glitchtip-web:8080/<project-id>
   ```
   > Use `glitchtip-web:8080` (Docker internal), **not** `localhost:8090` — the Django container resolves Docker service names, not host ports.
7. Restart the backend:
   ```bash
   docker compose restart backend
   ```

### What gets tracked

| Feature | How |
|---|---|
| Exceptions | Automatically via `DjangoIntegration` |
| Performance | HTTP request transactions (`traces_sample_rate=1.0` in dev, `0.2` in prod) |
| Logs | `ERROR`-level Python logs forwarded as events via `LoggingIntegration` |
| Redis errors | Via `RedisIntegration` |

### Verify the connection

```bash
docker compose exec backend python -c "
import sentry_sdk
sentry_sdk.init(dsn='<your-dsn-with-glitchtip-web-host>')
try:
    raise ValueError('GlitchTip connectivity test')
except Exception as e:
    sentry_sdk.capture_exception(e)
sentry_sdk.flush(timeout=5)
print('Done — check http://localhost:8090')
"
```

### Services

| Container | Role |
|---|---|
| `glitchtip-web` | Web UI + API (port 8090 on host) |
| `glitchtip-worker` | Background task processor (event ingestion, alerts, uptime checks) |
| `glitchtip-db` | Dedicated PostgreSQL 16 instance |
| `glitchtip-migrate` | One-shot migration runner — runs on `docker compose up`, then exits |

---

## Matomo — Web Analytics

Matomo is a self-hosted Google Analytics alternative. It tracks frontend page views and events with full data ownership.

### First-time setup

1. Open http://localhost:8080
2. Follow the Matomo installation wizard
3. When prompted for database credentials, use the values from your `.env`:
   - Host: `matomo-db`
   - Login: value of `MYSQL_USER`
   - Password: value of `MYSQL_PASSWORD`
   - Database name: value of `MYSQL_DATABASE`
4. Complete the wizard to create your admin account and add your first website
5. Copy the **JavaScript tracking code** and add it to the Vue frontend (`wetravel-front`)

### Services

| Container | Role |
|---|---|
| `matomo` | Web UI + tracker (port 8080 on host) |
| `matomo-db` | MariaDB 10.11 database |

> Matomo data is persisted in Docker volumes (`matomo_data`, `matomo_db_data`) and survives container restarts.

---

## Useful Commands

```bash
# View logs for a specific service
docker compose logs -f backend
docker compose logs -f glitchtip-worker
docker compose logs -f matomo

# Run Django management commands
docker compose exec backend python manage.py <command>

# Open a Django shell
docker compose exec backend python manage.py shell

# Open a psql shell (WeTravel DB)
docker compose exec db psql -U wetravel -d wetravel

# Open a psql shell (GlitchTip DB)
docker compose exec glitchtip-db psql -U glitchtip -d glitchtip

# Rebuild the backend image after dependency changes
docker compose build backend

# Stop all services
docker compose down

# Stop and delete all volumes (full reset — destructive)
docker compose down -v
```

---

## API Endpoints

Full interactive docs at http://localhost:8000/api/schema/swagger-ui/

```
# Cities
GET    /api/cities/                         list + search (?q=paris, ?continent=europe)
GET    /api/cities/<slug>/                  city detail
GET    /api/cities/<slug>/comments/         paginated comments
POST   /api/cities/<slug>/comments/         post comment (auth required)

# Auth
POST   /api/auth/register/
POST   /api/auth/login/
POST   /api/auth/logout/
POST   /api/auth/token/refresh/
GET    /api/auth/google/
GET    /api/auth/google/callback/
GET    /api/auth/me/                        current user profile

# Booking
GET    /api/booking/search/?city=<slug>&checkin=<date>&checkout=<date>
```

---

## Project Structure

```
wetravel-back/
├── accounts/           # JWT auth views, cookie-based authentication
├── cities/             # City, Place, Comment models + API
│   ├── migrations/     # DB migrations (includes seed data)
│   └── management/
│       └── commands/
│           ├── fetch_places.py       # populate Place from Google Places API
│           └── fetch_city_images.py  # populate hero images from Unsplash / Google
├── users/              # Custom User model
├── wetravel_back/      # Django project settings, urls, wsgi
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```
