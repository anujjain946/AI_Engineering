# RoleMatrix — Django Multi-Role RBAC

A starter Django project implementing:
- Custom email login
- Multiple dynamic roles
- Role-wise permissions
- Dynamic sidebar menu
- Custom dashboard
- Django admin for managing users, roles and permissions

## 1. Requirements
- Python 3.10+
- pip
- Virtual environment recommended

## 2. Install
Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Windows:
```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_roles
```

## 4. Create admin
```bash
python manage.py createsuperuser
```
Use an email and password. The superuser can access `/admin/`.

## 5. Start
```bash
python manage.py runserver
```
Open:
- Login: http://127.0.0.1:8000/login/
- Dashboard: http://127.0.0.1:8000/
- Django admin: http://127.0.0.1:8000/admin/

## 6. Create normal users
Go to `/admin/` → Users → Add User. Set email, password and role.

Seeded roles:
- Admin: dashboard, users, reports, settings
- Manager: dashboard, users, reports
- Staff: dashboard, reports
- Customer: dashboard

## Architecture
accounts/
  models.py       # User, Role, Permission, RolePermission
  views.py        # email + role login
  admin.py
  management/     # seed command

dashboard/
  views.py        # permission-driven dashboard/menu

templates/
  base.html       # dynamic sidebar
  login.html
  dashboard.html

## Production notes
Before production:
- move SECRET_KEY to environment variables
- set DEBUG=False
- configure ALLOWED_HOSTS
- use PostgreSQL/MySQL
- add HTTPS/security settings
- add audit logs and API authentication if required

## Important
This is a clean starter/RBAC foundation, not a finished enterprise application. Add object-level permissions, APIs, password reset, email verification, rate limiting, audit logs and tests before production use.
