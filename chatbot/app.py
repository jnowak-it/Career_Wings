from anthropic import Anthropic
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import pandas as pd
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = Flask(__name__)

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["50 per day", "10 per hour"]
)

@app.route("/")
def strona_glowna():
    return render_template("index.html", aktywna_zakladka="pytanie")

@app.route("/zapytaj", methods=["POST"])
@limiter.limit("10 per hour")
def zapytaj():
    pytanie = request.form.get("pytanie")

    if pytanie is None or pytanie.strip() == "":
        return render_template("index.html", odpowiedz="Please enter a question", aktywna_zakladka="pytanie")

    if len(pytanie) > 1000:
        return render_template("index.html", odpowiedz="Your question is too long (max 1000 characters).", aktywna_zakladka="pytanie")

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": pytanie}]
        )
        odpowiedz = response.content[0].text

    except Exception as e:
        odpowiedz = f"Failed to get a response: {e}"

    return render_template("index.html", odpowiedz=odpowiedz, aktywna_zakladka="pytanie")

MAX_FILE_SIZE = 5 * 1024 * 1024 # 5 MB

@app.route("/analizuj", methods=["POST"])
@limiter.limit("5 per hour")
def analizuj():
    plik = request.files.get("plik_csv")

    if plik is None or plik.filename == "":
        return render_template("index.html", podsumowanie="Nie wybrano pliku", aktywna_zakladka="analiza")

    plik.seek(0, os.SEEK_END)
    file_size = plik.tell()
    plik.seek(0)

    if file_size > MAX_FILE_SIZE:
        return render_template("index.html", podsumowanie="File is too large (max 5 MB).", aktywna_zakladka="analiza")

    df = pd.read_csv(plik)
    dane_tekstowe = df.to_string()

    prompt = f"""Przeanalizuj poniższe dane z pliku CSV i napisz krótkie podsumowanie
    po polsku: jakie są główne wnioski, czy są jakieś nietypowe wartości, jakie
    wzorce widać w danych.
    
    Dane:
    {dane_tekstowe}"""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        podsumowanie = response.content[0].text
    except Exception as e:
        podsumowanie = f"Nie udało się wygenerować podsumowania: {e}"

    return render_template("index.html", podsumowanie=podsumowanie, aktywna_zakladka="analiza")
if __name__ == "__main__":
    app.run(debug=True, port=5001)