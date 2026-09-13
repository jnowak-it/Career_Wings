from anthropic import Anthropic
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = Flask(__name__)
@app.route("/")
def strona_glowna():
    return render_template("index.html", aktywna_zakladka="pytanie")

@app.route("/zapytaj", methods=["POST"])
def zapytaj():
    pytanie = request.form.get("pytanie")

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": pytanie}]
    )
    odpowiedz = response.content[0].text

    return render_template("index.html", odpowiedz=odpowiedz, aktywna_zakladka="pytanie")

@app.route("/analizuj", methods=["POST"])
def analizuj():
    plik = request.files.get("plik_csv")

    if plik is None or plik.filename == "":
        return render_template("index.html", podsumowanie="Nie wybrano pliku", aktywna_zakladka="analiza")

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