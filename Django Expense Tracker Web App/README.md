# Django Expense Tracker

Simple Django web app for tracking personal expenses. Authenticated users can create, view, update, and delete the  expenses themselves.

## Setup

```bash
python -m pip install Django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/login/` and log in.

## How to test

- **Login** at `/login/`
- **View list** at `/expenses/`
- **Add** at `/expenses/create/`
- **Edit** at `/expenses/<id>/edit/`
- **Delete** at `/expenses/<id>/delete/`

## Approach

- Uses Django’s built-in auth with a **custom user model** (`accounts.User`).
- Expense CRUD is implemented with **class-based views** and templates.
- All expense pages require authentication, and each query is restricted to the logged-in user.
- Uses Django **messages** framework for success feedback.
