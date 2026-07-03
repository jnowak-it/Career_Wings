#🇵🇱Napisz skrypt, który pyta użytkownika o imię i rok urodzenia, oblicza ile lat zostało do emerytury
#i wypisuje spersonalizowaną wiadomość.
#🇬🇧Write a script that asks the user for their name and year of birth, calculates how many years are left until retirement
#and return a personalized message.

#retirement after 60 years for women in Poland and 65 years for men in Poland

from datetime import datetime

def is_name_correct():
    while True:
        name = input("Enter your name: ").strip()
        if len(name) == 0 or not name.isalpha():
            print("Incorrect name. Please try again.")
        else:
            break
    return name

def is_year_correct():
    current_year = datetime.now().year
    while True:
        year_born = input("Enter year born: ")
        if not(year_born.isdigit() and 1000 <= int(year_born) <= current_year):
            print("Please enter a valid year.")
        else:
            break
    return int(year_born)


def what_gender():
    gender = input("Enter your gender: M for male, F for female: ").upper()
    return gender

def is_age_correct():
    current_year = datetime.now().year
    age = current_year - is_year_correct()
    retirement_age_women = 60
    retirement_age_men = 65
    if (age >= retirement_age_men and what_gender() == "M") or (age >= retirement_age_women and what_gender() == "F"):
        return True
    else:
        return False

def can_retire():
    is_name_correct()
    is_year_correct()
    what_gender()
    is_age_correct()

can_retire()


