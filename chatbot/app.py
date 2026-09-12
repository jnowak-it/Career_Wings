from anthropic import Anthropic
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTROPHIC_API_KEY"))

app = Flask(__name__)
@app.route("/")
def strona_glowna():
    return render_template("index.html")
@app.route("/zapytaj", methods=["POST"])
def zapytaj():
    pytanie = request.form.get("pytanie")

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": pytanie}]
    )
    odpowiedz = response.content[0].text

    return render_template("index.html", odpowiedz=odpowiedz)
if __name__ == "__main__":
    app.run(debug=True, port=5001)