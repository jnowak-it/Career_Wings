import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

MODEL = "claude-sonnet-4-5"

def main():
    historia = []
    print("Wpisz pytanie lub napisz 'quit' aby zakończyć.\n")

    while True:
        pytanie = input("Ty: ").strip()
        if pytanie.lower() == "quit":
            print("Koniec sesji. Do zobaczenia!")
            break
        if not pytanie:
            continue
        historia.append({"role": "user", "content": pytanie})

        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=1024,
                messages=historia,
            )

            odpowiedz = response.content[0].text
            print(f"\nClaude: {odpowiedz}\n")

            historia.append({"role": "assistant", "content": odpowiedz})

        except Exception as e:
            print(f"\nWystąpił błąd podczas komunikacji z API: {e}\n")
            historia.pop()

if __name__ == "__main__":
    main()
