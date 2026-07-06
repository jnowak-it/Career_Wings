#🇵🇱Napisz skrypt, który pyta użytkownika o imię i rok urodzenia, oblicza ile lat zostało do emerytury
#i wypisuje spersonalizowaną wiadomość.
#🇬🇧Write a script that asks the user for their name and year of birth, calculates how many years are left until retirement
#and return a personalized message.

#retirement after 60 years for women in Poland and 65 years for men in Poland

from datetime import datetime

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if len(name) == 0 or not name.isalpha():
            print("Incorrect name. Please try again.")
        else:
            break
    return name

def get_valid_year():
    current_year = datetime.now().year
    while True:
        year_born = input("Enter year born: ")
        if not(year_born.isdigit() and 1900 <= int(year_born) <= current_year):
            print("Please enter a valid year.")
        else:
            break
    return int(year_born)

def get_valid_gender():
    while True:
        gender = input("Enter your gender: M for male, F for female: ").upper()
        if gender not in ["M", "F"]:
            print("Please enter a valid gender.")
        else:
            break
    return gender

def retirement_check():
    name = get_valid_name()
    year_born = get_valid_year()
    gender = get_valid_gender()
    current_year = datetime.now().year
    age = current_year - year_born
    retirement_age_women = 60
    retirement_age_men = 65
    if (age >= retirement_age_men and gender == "M") or (age >= retirement_age_women and gender == "F"):
        print(f"{name}, you can retire.")
    else:
        if gender == "M":
            years_left = retirement_age_men - age
        else:
            years_left = retirement_age_women - age
        print(f"{name}, you cannot retire. You can retire in {years_left} years.")

retirement_check()

