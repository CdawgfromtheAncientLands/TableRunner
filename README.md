# TableRunner

Web app for detailed, automated TTRPG travel in an overworld.

This repository now includes a minimal [Django](https://www.djangoproject.com/) project
called `tablerunner` with a single app named `travels`. The default view
returns a simple "Hello, TableRunner!" response.

## Getting Started

1. Install dependencies (requires Python 3.12+):

   ```bash
   pip install -r requirements.txt
   ```

2. Run database migrations and start the development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. Open `http://127.0.0.1:8000/` in your browser to see the welcome page.

## Requirements

All Python dependencies are listed in `requirements.txt`.
