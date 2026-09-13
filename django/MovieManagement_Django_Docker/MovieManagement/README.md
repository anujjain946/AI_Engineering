# MovieManagement — Django RBAC Starter

A production-oriented Django starter with:

1. Custom user model
2. Roles + permissions + user-role mapping
3. User login/logout/dashboard
4. Separate custom Django admin login/dashboard
5. Dynamic menu controlled from the admin site
6. PostgreSQL
7. Docker + Docker Compose
8. Adminer

## Architecture

- `accounts/` — custom user
- `rbac/` — Role, Permission, RolePermission, UserRole
- `menus/` — dynamic MenuItem
- `core/` — user dashboard, API and custom admin site
- `config/` — Django project configuration

## Start

Copy environment file:

```bash
cp .env.example .env
```

Build and run:

```bash
docker compose up --build
```

Application:

- http://localhost:8000/
- User login: http://localhost:8000/login/
- Custom admin: http://localhost:8000/admin/
- Adminer: http://localhost:80808/

## Adminer connection

Use:

- System: `PostgreSQL`
- Server: `db`
- Username: `postgres`
- Password: `postgres`
- Database: `movie_management`

Do NOT use `localhost` as the Adminer database server because Adminer runs in its own container.

## Demo accounts

Admin:

- Username: `admin`
- Password: `Admin@123`

Normal user:

- Username: `user`
- Password: `User@123`

Change these passwords immediately for real deployment.

## Dynamic menu

Menu records are stored in `menus_menuitem`.

From custom admin:

`http://localhost:8000/admin/`

Open **Menu items** and control:

- Name
- URL name
- Required permission
- Sort order
- Active/inactive

Example:

`Movies` → permission `movies.view`

Only users with that permission see the menu item.

## API

Authenticated endpoints:

```text
GET /api/me/
GET /api/menus/
```

## Important next modules

For the full Movie Management product, add:

- Movie
- Genre
- Cast
- Director
- Review
- Rating
- Search/filter/pagination
- JWT authentication for mobile/API clients
- Audit logs
- Soft delete
- Object-level permissions
