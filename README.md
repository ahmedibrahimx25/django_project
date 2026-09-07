# Todo API

A simple Task/Process REST API built with Django + Django REST Framework.

## Endpoints

| Method | URL            | Action            |
|--------|----------------|-------------------|
| GET    | `/`            | List all processes |
| GET    | `/<id>/`       | Retrieve one process |

## Local setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deployment (Cloudflare Pages)

Build command:

```
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

Start command:

```
gunicorn todo.wsgi
```

The `SECRET_KEY` and `DEBUG` values in `settings.py` are for development only.