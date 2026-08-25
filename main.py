from joke_service import *
from translation_service import *
from bidi.algorithm import get_display

def choose_language():
    language = {
        "1": "he",
        "2": "es",
        "3": "fr",
        "4": "it"}

    while True:
        print("choose a translation language:")
        print("1. Hebrew")
        print("2. Spanish")
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
        joke = extract_joke_data(joke_data)
        analysis = analyze_joke(joke["joke"])

        translation_data = translate_joke(joke["joke"], language)
        translated_joke = extract_translation(translation_data)
        print("\n translation response:")
        print(translation_data)

        print("\nTranslation:")
        print(get_display(translated_joke))

        print("\nSafe programming joke:")
        print(joke["joke"])

        print("\n Joke informtion:")
        print(f"Category: {joke['category']}")
        print(f"Joke ID: {joke['joke_id']}")
        print(f"Language: {joke['language']}")
        print(f"Words: {analysis['words']}")
        print(f"Characters: {analysis['characters']}")



main()