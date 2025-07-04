# Bug Tracker
This is a Django project for tracking the bug reports.

## Getting Started
This project is set up to use Django with Poetry for dependency management. 
Follow the instructions below to get started.

## Prerequisites
- Python 3.12 or higher
- Poetry
- Git

## Installation
1. Clone the repository `git clone git@github.com:piotrfura/bug_tracker.git`
2. Navigate to the project directory `cd bug_tracker`
3. Set up and activate the virtual environment `python3 -m venv venv && source venv/bin/activate`
4. Install dependencies `poetry install`
5. Run migrations to set up the database `python3 manage.py migrate`
6. Run the Django development server `python3 manage.py runserver`
