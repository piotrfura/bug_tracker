# Bug Tracker ![Bug Tracker Logo](static_files/icon/bug-tracker-32x32.png)
This is a Django project for tracking the bug reports.

## Getting Started
This project is set up to use Django with Poetry for dependency management. 

Follow the instructions below to get started or go to the working instance at [bugtracker.piotrfura.pl](https://bugtracker.piotrfura.pl).

## Features
- Create and list bug reports.
- User-friendly forms with `django-crispy-forms`.
- Content moderation for bug report submissions using OpenAI's Moderation API to prevent inappropriate content.

## Prerequisites
- Python 3.12 or higher
- Poetry
- Git

## Local Development Setup
1. Clone the repository `git clone git@github.com:piotrfura/bug_tracker.git`
2. Navigate to the project directory `cd bug_tracker`
3. Set up and activate the virtual environment `python3 -m venv venv && source venv/bin/activate`
4. Install dependencies `poetry install`
5. Create a `.env` file in the root directory with the content based on the `.env.example` file. Make sure to set the `SECRET_KEY`, `DEBUG`, and `OPENAI_API_KEY` variables appropriately.
6. Run migrations to set up the database `python3 manage.py migrate`
7. Run the Django development server `python3 manage.py runserver`
8. Access the application at `http://localhost:8000`

## Deployment using Docker
To deploy the project, you can use a docker container. 
The Dockerfile is set up to run the Django application with Gunicorn.
### Steps to Deploy
1. Clone the repository `git clone git@github.com:piotrfura/bug_tracker.git`
2. Build the Docker image `docker build --platform=linux/amd64 -t bug_tracker-amd64 .`
3. Create a `.env.prod` file in the root directory with the content based on the `.env.example` file. Make sure to set the `SECRET_KEY`, `DEBUG`, and `OPENAI_API_KEY` variables appropriately.
4. Create a `.env.db` file in the root directory with the content based on the `.env.db.example` file. 
5. Run the Docker container `docker compose up -d`
6. Access the application at `http://localhost:8009` or the port specified in your `docker-compose.yml` file. 

To run the application in production, you can use a reverse proxy like Nginx or Apache to serve the static files and proxy requests to the Gunicorn server.
