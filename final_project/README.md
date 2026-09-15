# AI Flashcards

A web app that turns your study notes into flashcards using Claude, with
user accounts and a simple study mode.

## Features

- User registration and login (passwords hashed with Werkzeug)
- Paste study text → AI generates a flashcard set (question/answer pairs)
- Each user only sees their own flashcard sets
- Study mode: click a card to flip between question and answer
- Input length validation
- Rate limiting on the AI-calling route (Flask-Limiter)
- System prompt guardrails + response filtering against prompt injection

## Setup

1. Clone the repo and enter the folder:
   ```bash
   git clone <your-repo-url>
   cd ai_flashcards
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in your own values:
   ```bash
   cp .env.example .env
   ```

5. Create the database tables:
   ```bash
   python
   >>> from app import app, db
   >>> with app.app_context():
   ...     db.create_all()
   ...
   >>> exit()
   ```

6. Run the app:
   ```bash
   python app.py
   ```
   Visit `http://127.0.0.1:5002`.

## Deployment

This app includes a `Procfile` for deployment on Render or Railway.
Set the `ANTHROPIC_API_KEY` and `SECRET_KEY` environment variables in your
hosting provider's dashboard — never commit real values in `.env`.
