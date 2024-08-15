# Tanmya Vishvakarma PyjamaHR Submission

## Deployed Application

The deployed application and the API Collections are accessible at: [PyjamaHR Submission](https://tanmya-pyjamahr-submission.onrender.com)

## Prerequisites

Ensure you have the following installed:

- Python 3.9
- Docker
- Docker Compose
- Git

## Clone the Repository

```bash
git clone https://github.com/tanmyavishvakarma/tanmya-pyjamahr-submission.git
cd tanmya-pyjamahr-submission
```

## Environment Variables

Create a `.env` file in the root directory of the project with the following content:

```bash
# Django Secret Key
SECRET_KEY='your_django_secret_key'

# Database Configuration
DB_NAME='your_db_name'
DB_USERNAME='your_db_username'
DB_PASSWORD='your_db_password'
DB_HOSTNAME='your_db_hostname'
DB_PORT='your_db_port'
DB_URL='your_db_url'

# Email Configuration
EMAIL_USER='your_email_user'
EMAIL_PASSWORD='your_email_password'

# Redis Configuration
REDIS_URL='your_redis_url'
```

## Docker Setup

The project uses Docker and Docker Compose to set up the environment. 

1. **Build and Run the Containers**

    ```bash
    docker-compose up --build
    ```

2. **Migrate the Database**

    This step is handled automatically by the Docker setup during the container startup. If you need to run migrations manually:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

3. **Create a Superuser**

    You may want to create an admin user to access the Django admin:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

## Running Celery

Celery is configured to work with Redis as a broker. The `docker-compose.yml` file is already set up to start a Celery worker.

To check Celery logs:

```bash
docker-compose logs celery
```

## Accessing the Application

- **Web Application:** `http://localhost:8000`
- **Django Admin:** `http://localhost:8000/admin`

## Running Tests

To run the tests:

```bash
docker-compose exec web python manage.py test
```

## Stopping the Containers

When you're done, you can stop the containers with:

```bash
docker-compose down
```
---