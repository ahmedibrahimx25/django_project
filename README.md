# Django Process REST API on Cloudflare Workers

A Django + Django REST Framework API exposing the `Process` model, deployed to
Cloudflare Workers (Python) with a D1 database backend via
[`django-cf`](https://github.com/cloudflare/workers-py/tree/main/packages/django-cf).

## Endpoints

| Method | URL          | Action             |
|--------|--------------|--------------------|
| GET    | `/`          | List all processes |
| GET    | `/api/<id>/` | Retrieve one process |

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)
- [Node.js](https://nodejs.org/) (for wrangler)

## Local development

```sh
npm install
uv run pywrangler d1 migrations apply django-project-d1 --local
uv run pywrangler dev
```

The Worker runs locally at `http://localhost:8787`.

## Deploy to Cloudflare

1. Create a D1 database in the Cloudflare dashboard, e.g. `django-project-d1`.
2. Copy its database ID into `wrangler.jsonc` (`d1_databases[0].database_id`).
3. Apply migrations and deploy:

   ```sh
   uv run pywrangler d1 migrations apply django-project-d1 --remote
   npm run deploy
   ```

## Notes

- Schema changes are managed by hand-written Wrangler D1 SQL migrations in
  `migrations/`, not Django's `manage.py migrate`. See the official
  [django-todo-d1](https://github.com/cloudflare/python-workers-examples/tree/main/django-todo-d1)
  example.
- CORS is enabled for all origins via `src/task/middleware.py`.
- `SECRET_KEY` is a development placeholder; set a real value as a Worker secret
  when going to production.