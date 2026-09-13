# Role-Based Django Application

A Django application featuring email-based authentication, three user roles (Admin, Manager, Customer), database-driven dynamic menus, and automatic dashboard redirection by role.

## Features

- Custom user model: email login, contact number, role, and password.
- Three roles: Admin, Manager, Customer.
- Role-specific dashboard after login.
- Dynamic database-driven sidebar menu with role visibility settings.
- Django admin interface for users, roles, and menu items.
- Nested (parent/child) menu support.
- Bootstrap 5 responsive frontend.

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create migrations and database tables:

```bash
python manage.py makemigrations accounts core
python manage.py migrate
```

4. Create an administrator account:

```bash
python manage.py createsuperuser
```

Enter an email address, username, and password when prompted. Set the user role to `admin` through `/admin/` after signing in, if necessary.

5. Run the server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Add Dynamic Menus

1. Sign in at `http://127.0.0.1:8000/admin/`.
2. Create one **Role Assignment** for each role: `admin`, `manager`, and `customer`.
3. Create **Menu Items** with a title, URL, icon class, display order, and selected roles.
4. Leave the **Visible to roles** field blank to show a menu item to every authenticated role.
5. Optionally set a parent menu item to create a submenu.

### Example menus

| Title | URL | Icon | Roles |
|---|---|---|---|
| Dashboard | /dashboard/ | fa-tachometer-alt | All (leave blank) |
| User Management | /admin/accounts/user/ | fa-users | admin |
| Team | /manager-dashboard/ | fa-user-tie | admin, manager |
| My Account | /customer-dashboard/ | fa-user | customer |

## Role Redirects

| Role | Dashboard URL |
|---|---|
| Admin | `/admin-dashboard/` |
| Manager | `/manager-dashboard/` |
| Customer | `/customer-dashboard/` |

## Important Security Note

The registration page currently allows users to choose any role so you can test the feature easily. In a production app, remove the role field from public registration and assign privileged roles only from Django admin or via a secure approval workflow.
