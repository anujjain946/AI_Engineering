#!/bin/sh
set -e

python manage.py migrate
python manage.py seed_rbac
python manage.py seed_menu

exec "$@"
