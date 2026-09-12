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
    podglad = df.head().to_string()

    return render_template("index.html", podsumowanie=f"Wczytano plik. Podgląd danych:\n{podglad}", aktywna_zakladka="analiza")
if __name__ == "__main__":
    app.run(debug=True, port=5001)