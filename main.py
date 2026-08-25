from joke_service import *

def choose_language():
    language = {
        "1": "he",
        "2": "es",
        "3": "fr",
        "4": "it"}

    while True:
        print("choose a translation language:")
        print("1. Hebrew")
        print("2. English")
        print("3. French")
        print("4. Italian")

        choice = input("Enter your choise: ")

        if choice in language:
            return language[choice]

        print("Invalid language choice.")
        

def main():
    language = choose_language()

    if language:
        print(f"You chose: {language}")

    joke_data = get_safe_joke()

    if joke_data:
        print("\nSafe programming joke:")
        print(joke_data["joke"])
    else:
        print("Could not get a safe joke.")


main()