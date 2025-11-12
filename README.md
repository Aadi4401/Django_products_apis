# django_products

Django Products API — CRUD with JWT auth, soft delete, disable, export, bulk create.

## Quick start

1. Create venv: `python -m venv venv`
2. Activate: `source venv/bin/activate` (Linux/mac) or `.\venv\Scripts\Activate.ps1` (Windows)
3. Install: `pip install -r requirements.txt`
4. Migrations: `python manage.py makemigrations`
5. Migrate: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run: `python manage.py runserver`
8.Swagger: 'http://127.0.0.1:8000/swagger/'

the delete api soft deletes the product and product listing api shows the active ones so when soft delete is_active will be false so you'll se empty list there.