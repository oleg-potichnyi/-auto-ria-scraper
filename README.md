# auto-ria Scraper Project

This is a Python application designed to periodically scrape the AutoRia platform for used car listings. It collects data from each car card, storing it in a PostgreSQL database. Additionally, the application performs a daily database dump at a specified time, ensuring data integrity and providing backup functionality.

## Features

* Periodic scraping of the AutoRia platform for used cars.
* Data storage in a PostgreSQL database
* No duplicate entries are stored in the database.
* Daily database dumps stored in the "dumps" folder for backup purposes.
* Docker-compose deployment for easy setup and deployment.
* Environment settings stored in a .env file for configuration flexibility.

## Technology stack

* Backend:
  - Language: Python 3 
  - Framework: Django 
  - Database: Postgresql 
* Dependency Management: pip
* Virtual Environment: venv
* Database Migrations: Django Migrations
* Collaboration and Version Control:
  - Version Control System: Git
  - Repository Hosting: GitHub
* Task Queue: Celery
  - Message Broker: Redis 
* Environment Variables: .env
* Other: requirements.txt

## Environment Variables

This project uses environment variables for sensitive information and configuration. Two files, `.env` and `.env_sample`, are provided:

- `.env_sample` serves as a template with variable descriptions.
- Create a copy of `.env_sample` and name it `.env` to set your environment-specific configuration.
- Fill in the values for each variable in `.env`.
- Keep `.env` secure and add it to your `.gitignore` to prevent accidental commits.

Never commit the `.env` file to your version control system.

## Installation

Python3 must be already installed

```shell
- Сreate venv: "python3 -m venv venv"
# Activate the virtual environment on Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
- Install requirements: "pip install -r requirements.txt"
- Run migrations: "python manage.py migrate"
- Run Redis Server: "docker run -d -p 6379:6379 redis"
- Run celery worker for tasks handling: "celery -A auto_ria worker -l INFO"
- Run celery beat for tasks scheduling: "celery -A auto_ria beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler"
- Run app: "python manage.py runserver"
```

## User credentials

```shell
name: Oleg
password: user12345
```
