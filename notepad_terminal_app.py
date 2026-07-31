#🇵🇱 Zbuduj notatnik działający w terminalu. Można dodawać notatki, wyświetlać ich listę i usuwać wybrane.
#Wszystko zapisuje się do pliku JSON, więc dane nie giną po zamknięciu programu.
#🇬🇧 Build a notepad that runs in the terminal. You can add notes, view a list of them and delete selected ones.
#Everything is saved to JSON file, so your data won't be lost when you close the program.
import itertools
import json
from colorama import Fore, Style, init
init(autoreset=True)

def display_meny():
    print(Fore.LIGHTBLUE_EX + "\n==== Notes ====")
    print("1. Add a note")
    print("2. List all notes")
    print("3. Remove a note")
    print("4. Exit")
    return input(Fore.CYAN + "Choose an option (1-4): ")

def convert_to_json(notes):
    with open("notes.json", "w") as json_file:
        json.dump(notes, json_file)

def add_note(notes):
    title = input("Enter the note title: ")
    note = input("Enter the note content: ")
    notes[title] = note
    print(Fore.GREEN + "Note added: " + notes[title])

def list_notes(notes):
    if not notes:
        print(Fore.RED + "No notes added. Add one with option 1 in menu.")
        return
    print(Fore.LIGHTCYAN_EX + "\nYour notes:")
    for i, title in enumerate(notes, 1):
        print(f"{i}. {title}")

def delete_note(notes):
    if not notes:
        print(Fore.RED + "No notes to delete. Add one with option 1 in menu.")
        return
    list_notes(notes)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(notes):
            del notes[next(itertools.islice(notes, index, None))]
            print(Fore.GREEN + "Note deleted.")
        else:
            print(Fore.RED + "Invalid task number. Try again.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

def main():
    notes = {}
    print(Fore.MAGENTA + "\nWelcome to the notes app")

    while True:
        choice = display_meny()
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            convert_to_json(notes)
            print(Fore.MAGENTA + "\nExiting...")
            break
        else:
            print(Fore.RED + "\nInvalid choice, please try again")

if __name__ == "__main__":
    main()
