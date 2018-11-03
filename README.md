# Choban package manager


### Requirements
- Python & pip
- Postgres Database

### Database setup
Set these keys on your enviroment from .env  (You can rename .env.examle to .env)
- DATABASE_HOST
- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASSWORD

### Install dependencies
1. Install pip dependencies with `pip install -r requirements.txt`


### Installation
1. `python manage.py migrate`
3. `python manage.py runserver`


### Docker setup
1. Run docker-compose build && docker-compose up
