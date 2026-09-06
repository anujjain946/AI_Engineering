# Docker Beginner to Advanced — Django Practical Project

A complete practical Docker guide for Python/Django developers.

---

# 1. Docker Kya Hai?

Docker ek **containerization platform** hai.

Simple language mein:

> Docker application + dependencies + configuration ko ek isolated container mein run karta hai.

Example:

Without Docker:

```text
My Laptop
 ├── Python 3.12
 ├── Django
 ├── MySQL
 ├── Redis
 └── Other dependencies
```

Team member ke laptop par:

```text
My Laptop
 ├── Python 3.11
 ├── Different Django version
 ├── Different MySQL
 └── Errors 😵
```

Docker ke saath:

```text
Docker
 ├── Django Container
 ├── MySQL Container
 └── Redis Container
```

Sabka environment controlled rahega.

---

# 2. Docker ke Important Concepts

Docker seekhne ke liye ye concepts important hain:

```text
Docker
│
├── Image
├── Container
├── Dockerfile
├── Docker Compose
├── Volume
├── Network
├── Port
├── Environment Variables
├── Registry
└── Docker Hub
```

---

# 3. Image

Image ek **blueprint/template** hoti hai.

Example:

```text
python:3.12
mysql:8.0
redis:7
nginx:latest
```

Image se container create hota hai.

```text
Image
   ↓
Container
```

Example:

```bash
docker pull python:3.12
```

---

# 4. Container

Container image ka running instance hai.

Example:

```bash
docker run python:3.12
```

Image:

```text
python:3.12
```

Running container:

```text
python-container
```

Check containers:

```bash
docker ps
```

All containers:

```bash
docker ps -a
```

---

# 5. Docker Installation

Ubuntu:

```bash
sudo apt update
sudo apt install docker.io
```

Check:

```bash
docker --version
```

Docker service:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Test:

```bash
docker run hello-world
```

---

# 6. Important Docker Commands

## Images

List images:

```bash
docker images
```

Download image:

```bash
docker pull python:3.12
```

Remove image:

```bash
docker rmi IMAGE_ID
```

---

## Containers

Run:

```bash
docker run python:3.12
```

List running:

```bash
docker ps
```

List all:

```bash
docker ps -a
```

Stop:

```bash
docker stop CONTAINER_ID
```

Start:

```bash
docker start CONTAINER_ID
```

Restart:

```bash
docker restart CONTAINER_ID
```

Remove:

```bash
docker rm CONTAINER_ID
```

Container logs:

```bash
docker logs CONTAINER_ID
```

Enter container:

```bash
docker exec -it CONTAINER_ID bash
```

---

# 7. Docker Port

Suppose Django container ke andar:

```text
8000
```

Host machine par bhi:

```text
8000
```

Mapping:

```text
Host 8000 → Container 8000
```

Command:

```bash
docker run -p 8000:8000 myapp
```

General syntax:

```text
-p HOST_PORT:CONTAINER_PORT
```

---

# 8. Dockerfile

Dockerfile batata hai ki Docker image kaise banani hai.

Example:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

# 9. Dockerfile Explanation

## FROM

```dockerfile
FROM python:3.12-slim
```

Base image Python ki hai.

---

## WORKDIR

```dockerfile
WORKDIR /app
```

Container ke andar working directory:

```text
/app
```

---

## COPY

```dockerfile
COPY requirements.txt .
```

Local file container mein copy hoti hai.

---

## RUN

```dockerfile
RUN pip install -r requirements.txt
```

Image build ke time command execute hoti hai.

---

## EXPOSE

```dockerfile
EXPOSE 8000
```

Application ka port document karta hai.

---

## CMD

```dockerfile
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

Container start hone par Django run karega.

---

# 10. Docker Image Build

Dockerfile ke folder mein:

```bash
docker build -t django-app .
```

Check:

```bash
docker images
```

Run:

```bash
docker run -p 8000:8000 django-app
```

Browser:

```text
http://localhost:8000
```

---

# 11. .dockerignore

Docker ko unnecessary files copy nahi karni chahiye.

Create:

```text
.dockerignore
```

Example:

```text
.git
.gitignore
__pycache__
*.pyc
*.pyo
.env
venv
.venv
db.sqlite3
.idea
.vscode
```

---

# 12. Environment Variables

Secrets ko Dockerfile mein directly nahi likhna chahiye.

Bad:

```python
PASSWORD = "mypassword"
```

Better:

```python
import os

PASSWORD = os.getenv("DB_PASSWORD")
```

`.env`:

```env
DEBUG=True

DB_NAME=ims_db
DB_USER=ims_user
DB_PASSWORD=secret
DB_HOST=db
DB_PORT=3306
```

---

# 13. Docker Compose

Agar Django + MySQL + Redis jaise multiple services hain, manually containers manage karna difficult ho sakta hai.

Docker Compose use karte hain.

Architecture:

```text
                 Docker Compose
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
    Django          MySQL          Redis
   Container       Container       Container
```

---

# 14. Django + MySQL Docker Project

Project structure:

```text
ims/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│
├── manage.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .env
```

---

# 15. requirements.txt

Example:

```text
Django
djangorestframework
mysqlclient
python-dotenv
gunicorn
```

Production project mein versions pin karna better hai:

```text
Django==6.1
djangorestframework==3.16.1
mysqlclient==2.2.8
gunicorn==23.0.0
python-dotenv==1.1.1
```

---

# 16. Django Dockerfile

Create:

```text
Dockerfile
```

Content:

```dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
       default-libmysqlclient-dev \
       build-essential \
       pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

# 17. Docker Compose

Create:

```text
docker-compose.yml
```

Example:

```yaml
services:

  web:
    build: .
    container_name: django_app
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: mysql:8.0
    container_name: mysql_db
    restart: always
    environment:
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    ports:
      - "3307:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

---

# 18. Why MySQL Port 3307?

Container ke andar MySQL:

```text
3306
```

Host machine:

```text
3307
```

Mapping:

```text
localhost:3307
        ↓
Docker MySQL:3306
```

Django container se MySQL connect karte waqt:

```text
DB_HOST=db
DB_PORT=3306
```

Important:

> Django container ke andar `localhost` MySQL container ko refer nahi karta.

Use:

```text
db
```

because `db` Compose service ka naam hai.

---

# 19. .env

Create:

```text
.env
```

```env
DEBUG=True

DB_NAME=ims_db
DB_USER=ims_user
DB_PASSWORD=ims_password
DB_ROOT_PASSWORD=root_password

DB_HOST=db
DB_PORT=3306
```

`.env` ko Git mein commit mat karo.

`.gitignore`:

```text
.env
```

---

# 20. Django Database Settings

`settings.py`:

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT", "3306"),
    }
}
```

---

# 21. Start Docker Project

Build:

```bash
docker compose build
```

Start:

```bash
docker compose up
```

Background:

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

Logs:

```bash
docker compose logs
```

Web logs:

```bash
docker compose logs web
```

DB logs:

```bash
docker compose logs db
```

---

# 22. Django Migrations

Container ke andar migration:

```bash
docker compose exec web python manage.py makemigrations
```

Then:

```bash
docker compose exec web python manage.py migrate
```

Create superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

---

# 23. Django Shell

```bash
docker compose exec web python manage.py shell
```

---

# 24. Run Tests

```bash
docker compose exec web python manage.py test
```

---

# 25. Django Container mein Bash

```bash
docker compose exec web bash
```

Now:

```bash
ls
```

You will see:

```text
manage.py
config
users
requirements.txt
```

Exit:

```bash
exit
```

---

# 26. MySQL Container Access

```bash
docker compose exec db mysql -u root -p
```

Or:

```bash
docker exec -it mysql_db mysql -u root -p
```

---

# 27. Docker Volume

Container delete hone par normally container ka internal data delete ho sakta hai.

MySQL data ko persist karne ke liye volume:

```yaml
volumes:
  - mysql_data:/var/lib/mysql
```

Architecture:

```text
MySQL Container
       │
       ↓
 mysql_data volume
```

Container recreate hone ke baad bhi database data available rahega.

List volumes:

```bash
docker volume ls
```

Inspect:

```bash
docker volume inspect mysql_data
```

---

# 28. Docker Network

Docker Compose automatically network create karta hai.

Example:

```text
django_app
    │
    │ Docker Network
    ↓
mysql_db
```

Django:

```env
DB_HOST=db
```

MySQL:

```text
db:3306
```

---

# 29. Important Concept: localhost

Docker mein ye common mistake hai:

```env
DB_HOST=localhost
```

Django container ke andar `localhost` ka meaning hai:

```text
Django container itself
```

MySQL ke liye:

```env
DB_HOST=db
```

because:

```yaml
services:
  db:
```

service name:

```text
db
```

---

# 30. Docker Compose Lifecycle

Start:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

Stop + remove volumes:

```bash
docker compose down -v
```

Rebuild:

```bash
docker compose up --build
```

Restart:

```bash
docker compose restart
```

---

# 31. Docker Logs

All:

```bash
docker compose logs
```

Follow logs:

```bash
docker compose logs -f
```

Django:

```bash
docker compose logs -f web
```

MySQL:

```bash
docker compose logs -f db
```

---

# 32. Docker Production Architecture

Development:

```text
Browser
   ↓
Django
   ↓
MySQL
```

Production:

```text
                    Internet
                       │
                       ↓
                    Nginx
                       │
                       ↓
                    Gunicorn
                       │
                       ↓
                    Django
                       │
              ┌────────┴────────┐
              ↓                 ↓
            MySQL             Redis
              │
              ↓
          Persistent
           Volume
```

---

# 33. Gunicorn

Development:

```bash
python manage.py runserver
```

Production:

```bash
gunicorn config.wsgi:application
```

Dockerfile production command:

```dockerfile
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

# 34. Nginx

Nginx generally handles:

```text
Internet
   ↓
Nginx
   ↓
Gunicorn
   ↓
Django
```

Nginx responsibilities:

* Reverse proxy
* Static files
* SSL termination
* Request handling
* Load balancing

---

# 35. Static Files

Django:

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Run:

```bash
docker compose exec web python manage.py collectstatic --noinput
```

Production mein Nginx static files serve kar sakta hai.

---

# 36. Multi-Container Architecture

Large Django project:

```text
                    NGINX
                      │
                      ↓
                Django/Gunicorn
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
      MySQL         Redis        Celery
                                    │
                                    ↓
                                  Worker
```

Example use:

```text
Django
  ↓
Celery Task
  ↓
Redis
  ↓
Worker
```

---

# 37. Redis

Redis ka use:

* Cache
* Session
* Celery broker
* Temporary data
* Rate limiting

Compose:

```yaml
redis:
  image: redis:7-alpine
  container_name: redis
```

Django se:

```text
redis://redis:6379/1
```

---

# 38. Celery

Example architecture:

```text
Django
   │
   ↓
Celery
   │
   ↓
Redis
   │
   ↓
Celery Worker
```

Long-running tasks:

* Email sending
* Report generation
* Image processing
* Notifications
* Background jobs

---

# 39. Docker Registry

Docker image ko online store karne ke liye registry use hoti hai.

Popular:

```text
Docker Hub
GitHub Container Registry
AWS ECR
Google Artifact Registry
Azure Container Registry
```

Example:

```bash
docker login
```

Build:

```bash
docker build -t username/ims-api:1.0 .
```

Push:

```bash
docker push username/ims-api:1.0
```

---

# 40. Docker Tags

Example:

```text
ims-api:1.0
ims-api:1.1
ims-api:latest
```

Better production practice:

```text
ims-api:2026.08.26
```

rather than relying only on:

```text
latest
```

---

# 41. Docker Healthcheck

Example:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
  interval: 30s
  timeout: 10s
  retries: 3
```

Healthcheck ka purpose:

```text
Healthy
Unhealthy
```

---

# 42. Docker Security Basics

Never put secrets directly into Dockerfile:

```dockerfile
ENV DB_PASSWORD=secret
```

Avoid.

Use:

```text
.env
Docker secrets
Cloud secret manager
```

Also:

```text
Don't run unnecessary services as root.
Don't expose MySQL publicly.
Don't commit .env.
Use minimal base images.
Keep images updated.
```

---

# 43. Development vs Production

## Development

```text
Django runserver
Docker Compose
Volume mount
DEBUG=True
Local MySQL
```

## Production

```text
Nginx
Gunicorn
Django
MySQL
Redis
Celery
HTTPS
DEBUG=False
Secrets
Monitoring
Backups
```

---

# 44. Practical Django IMS Project

For an Influencer Management System:

```text
                 NGINX
                   │
                   ↓
             Django API
                   │
       ┌───────────┼───────────┐
       ↓           ↓           ↓
     MySQL       Redis       Celery
       │                       │
       ↓                       ↓
   Application              Workers
      Data
```

Possible Django apps:

```text
ims/
│
├── users/
├── influencers/
├── campaigns/
├── brands/
├── customers/
├── payments/
├── notifications/
└── reports/
```

---

# 45. Example IMS API

Login:

```text
POST /api/auth/login/
```

Logout:

```text
POST /api/auth/logout/
```

Users:

```text
GET /api/users/
```

Influencers:

```text
GET /api/influencers/
POST /api/influencers/
PUT /api/influencers/{id}/
DELETE /api/influencers/{id}/
```

Campaigns:

```text
GET /api/campaigns/
POST /api/campaigns/
```

---

# 46. Docker IMS Structure

```text
ims/
│
├── config/
│
├── apps/
│   ├── users/
│   ├── influencers/
│   ├── campaigns/
│   └── payments/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .env
├── .gitignore
└── manage.py
```

---

# 47. Recommended Development Workflow

Step 1:

```bash
git clone project
```

Step 2:

```bash
cp .env.example .env
```

Step 3:

```bash
docker compose build
```

Step 4:

```bash
docker compose up -d
```

Step 5:

```bash
docker compose exec web python manage.py migrate
```

Step 6:

```bash
docker compose exec web python manage.py createsuperuser
```

Step 7:

Open:

```text
http://localhost:8000
```

---

# 48. Daily Docker Commands

These commands should become familiar:

```bash
docker ps
docker images
docker logs
docker exec
docker stop
docker start
docker rm
docker rmi
```

Docker Compose:

```bash
docker compose up
docker compose up -d
docker compose down
docker compose build
docker compose up --build
docker compose ps
docker compose logs
docker compose exec
```

Django:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py shell
docker compose exec web python manage.py test
```

---

# 49. Common Errors

## Error 1 — Port already in use

```text
Bind for 0.0.0.0:3306 failed
```

Check:

```bash
sudo lsof -i :3306
```

Or change host port:

```yaml
ports:
  - "3307:3306"
```

---

## Error 2 — Django cannot connect to MySQL

Wrong:

```env
DB_HOST=localhost
```

Correct:

```env
DB_HOST=db
```

---

## Error 3 — Container doesn't start

Check:

```bash
docker compose logs web
```

---

## Error 4 — Build cache problem

Try:

```bash
docker compose build --no-cache
```

---

## Error 5 — Permission problem

Check mounted files:

```bash
ls -la
```

Also check container user and file ownership.

---

# 50. Docker Volumes vs Bind Mount

## Volume

```yaml
volumes:
  - mysql_data:/var/lib/mysql
```

Docker manages storage.

Good for:

```text
Database
Persistent application data
```

## Bind Mount

```yaml
volumes:
  - .:/app
```

Host directory directly container mein mount hoti hai.

Good for:

```text
Development
Live code changes
```

---

# 51. Docker Build Optimization

Bad:

```dockerfile
COPY . .

RUN pip install -r requirements.txt
```

Better:

```dockerfile
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
```

Reason:

Docker layers cache karta hai.

Agar source code change hua hai but requirements nahi:

```text
pip install layer
       ↓
Cached
```

Build faster hoga.

---

# 52. Multi-stage Build

Advanced Docker mein multi-stage builds use kar sakte hain.

Concept:

```text
Builder Image
      ↓
Build dependencies
      ↓
Production Image
      ↓
Only required files
```

Benefits:

* Smaller image
* Less attack surface
* Faster deployment

---

# 53. Docker Debugging Process

Jab application work nahi kare:

### Step 1

```bash
docker compose ps
```

### Step 2

```bash
docker compose logs web
```

### Step 3

```bash
docker compose logs db
```

### Step 4

Enter container:

```bash
docker compose exec web bash
```

### Step 5

Check environment:

```bash
env
```

### Step 6

Check database:

```bash
python manage.py check
```

### Step 7

Test migration:

```bash
python manage.py migrate
```

---

# 54. Docker Learning Roadmap

## Level 1 — Beginner

Learn:

```text
Docker
Image
Container
Dockerfile
Port
Volume
Basic commands
```

Practice:

```bash
docker run nginx
docker run python
docker run mysql
```

---

## Level 2 — Intermediate

Learn:

```text
Docker Compose
Networks
Volumes
Environment variables
.dockerignore
Multi-container applications
```

Practice:

```text
Django + MySQL
```

---

## Level 3 — Advanced

Learn:

```text
Gunicorn
Nginx
Redis
Celery
Healthchecks
Multi-stage builds
Docker security
Image optimization
Private registries
```

Practice:

```text
Django
+
Nginx
+
Gunicorn
+
MySQL
+
Redis
+
Celery
```

---

# 55. Real-World Project Architecture

Final target:

```text
                         INTERNET
                            │
                            ↓
                         NGINX
                            │
                            ↓
                       GUNICORN
                            │
                            ↓
                    ┌──────────────┐
                    │    DJANGO    │
                    │   REST API   │
                    └──────┬───────┘
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
           MySQL         Redis         Celery
             │             │             │
             ↓             ↓             ↓
          Database        Cache        Workers
                                           │
                                           ↓
                                        Tasks
```

---

# 56. What You Should Build Practically

For your Django IMS project, build Docker in this order:

```text
Day 1
Docker basics
   ↓
Day 2
Dockerfile
   ↓
Day 3
Django + Docker
   ↓
Day 4
Django + MySQL
   ↓
Day 5
Docker Compose
   ↓
Day 6
Environment variables
   ↓
Day 7
Volumes + Networks
   ↓
Day 8
Redis
   ↓
Day 9
Celery
   ↓
Day 10
Nginx + Gunicorn
   ↓
Day 11
Production Docker setup
   ↓
Day 12
Docker security
   ↓
Day 13
Docker Hub / Registry
   ↓
Day 14
Deployment
```

---

# 57. Final Goal

Aapka Django project eventually is tarah run hona chahiye:

```bash
git clone <project>

cd ims

cp .env.example .env

docker compose up -d --build

docker compose exec web python manage.py migrate

docker compose exec web python manage.py createsuperuser
```

Then:

```text
Browser
   ↓
http://localhost
   ↓
Nginx
   ↓
Django
   ↓
MySQL
```

---

# 58. Most Important Docker Concepts to Remember

```text
IMAGE
↓
Blueprint

CONTAINER
↓
Running Image

DOCKERFILE
↓
Image banane ki instructions

COMPOSE
↓
Multiple containers manage karna

VOLUME
↓
Persistent data

NETWORK
↓
Containers ke beech communication

PORT
↓
Host ↔ Container communication

ENV
↓
Configuration / Secrets

REGISTRY
↓
Docker images store/share karna
```

---

# 59. Practical Project Checklist

* [ ] Install Docker
* [ ] Run hello-world
* [ ] Run Nginx container
* [ ] Learn docker ps
* [ ] Learn docker logs
* [ ] Learn docker exec
* [ ] Create Dockerfile
* [ ] Build Django image
* [ ] Run Django container
* [ ] Create docker-compose.yml
* [ ] Add MySQL
* [ ] Connect Django → MySQL
* [ ] Add `.env`
* [ ] Add Docker volume
* [ ] Add Docker network
* [ ] Run Django migrations
* [ ] Add Redis
* [ ] Add Celery
* [ ] Add Gunicorn
* [ ] Add Nginx
* [ ] Configure production settings
* [ ] Optimize Docker image
* [ ] Add healthchecks
* [ ] Push image to registry
* [ ] Deploy Dockerized Django application

---

# 60. Interview Questions

### Beginner

**Q1. Docker kya hai?**

Docker ek containerization technology hai jo application aur uski dependencies ko isolated containers mein package/run karti hai.

**Q2. Image aur Container mein difference?**

Image blueprint hai; container us image ka running instance hai.

**Q3. Dockerfile kya hai?**

Docker image create karne ke instructions ka file.

**Q4. Docker Compose kya hai?**

Multiple containers/services ko define aur manage karne ka tool.

**Q5. Volume kya hai?**

Container ke bahar persistent data store karne ka mechanism.

---

### Intermediate

**Q6. Docker network kaise kaam karta hai?**

Same Docker network par containers service name ke through ek doosre ko access kar sakte hain.

**Q7. Django container MySQL ko localhost se kyun access nahi karta?**

Because `localhost` Django container khud hota hai. Compose mein MySQL service name, e.g. `db`, use karna chahiye.

**Q8. `depends_on` kya karta hai?**

Compose ko service startup dependency batata hai.

**Q9. Docker volume aur bind mount mein difference?**

Volume Docker-managed storage hai; bind mount host filesystem ko container mein mount karta hai.

**Q10. Docker image ko optimize kaise karoge?**

* Small base image
* `.dockerignore`
* Layer caching
* Multi-stage builds
* Unnecessary packages avoid karna

---

### Advanced

**Q11. Production Django ke liye `runserver` kyun nahi?**

`runserver` development server hai. Production mein Gunicorn/Uvicorn jaise production application servers use kiye jaate hain.

**Q12. Nginx ka role kya hai?**

Reverse proxy, static file serving, SSL termination aur request routing.

**Q13. Redis ka use Django project mein?**

Caching, sessions, Celery broker aur temporary data ke liye.

**Q14. Celery ka use?**

Background/asynchronous tasks execute karne ke liye.

**Q15. Docker production architecture?**

```text
Nginx
 ↓
Gunicorn
 ↓
Django
 ↓
MySQL

Django
 ↓
Redis
 ↓
Celery Worker
```

---

# Conclusion

Docker ko sirf commands ke through mat seekho.

Best approach:

```text
Docker Basics
      ↓
Dockerfile
      ↓
Django Container
      ↓
Django + MySQL
      ↓
Docker Compose
      ↓
Volumes + Networks
      ↓
Redis + Celery
      ↓
Nginx + Gunicorn
      ↓
Production
      ↓
Deployment
```

**Aapke Django IMS project ke liye final target:** ek complete multi-container application jisme **Django REST API + MySQL + Redis + Celery + Nginx + Gunicorn + Docker Compose** ho.
