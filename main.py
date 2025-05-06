You said:
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Matej Kaplan
email: kaplan.matej1@seznam.cz
"""

# Uživatelé
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Texty pro analýzu
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Funkce pro přihlášení uživatele
def login():
    username = input("Zadejte přihlašovací jméno: ")
    password = input("Zadejte heslo: ")

    if username in users and users[username] == password:
        print(f"Ahoj {username}, vítejte zpět!")
        analyze_texts()
    else:
        print("Uživatel neexistuje nebo špatné heslo. Program bude ukončen.")

# Funkce pro výběr a analýzu textu
def analyze_texts():
    print("\nMáme pro tebe připravené 3 texty k analýze.")
    print("Vyber text zadáním čísla 1, 2 nebo 3.")
    
    choice = input("Zadejte číslo textu: ")

    if not choice.isdigit():
        print("Nezadali jste číslo. Program bude ukončen.")
        return

    choice = int(choice)

    if choice < 1 or choice > 3:
        print("Zadali jste neplatné číslo. Program bude ukončen.")
        return

    selected_text = TEXTS[choice - 1]
    print("\nVybraný text:")
    print(selected_text)

    # Jednoduchá analýza textu - počet slov
    word_count = len(selected_text.split())
    print(f"\nText obsahuje {word_count} slov.")

# Spuštění programu
login()  
Uprav tento kod tak aby:
Pro vybraný text spočítá následující statistiky:
počet slov,
počet slov začínajících velkým písmenem,
počet slov psaných velkými písmeny,
počet slov psaných malými písmeny,
počet čísel (ne cifer),
sumu všech čísel (ne cifer) v textu.


ChatGPT said:
Tady je upravený kód, který provádí podrobnější analýzu textu dle tvého zadání:

python
Copy
Edit
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Matej Kaplan
email: kaplan.matej1@seznam.cz
"""

# Uživatelé
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Texty pro analýzu
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Funkce pro přihlášení uživatele
def login():
    username = input("Zadejte přihlašovací jméno: ")
    password = input("Zadejte heslo: ")

    if username in users and users[username] == password:
        print(f"\nAhoj {username}, vítejte zpět!")
        analyze_texts()
    else:
        print("Uživatel neexistuje nebo špatné heslo. Program bude ukončen.")

# Funkce pro výběr a analýzu textu
def analyze_texts():
    print("\nMáme pro tebe připravené 3 texty k analýze.")
    print("Vyber text zadáním čísla 1, 2 nebo 3.")
    
    choice = input("Zadejte číslo textu: ")

    if not choice.isdigit():
        print("Nezadali jste číslo. Program bude ukončen.")
        return

    choice = int(choice)

    if choice < 1 or choice > 3:
        print("Zadali jste neplatné číslo. Program bude ukončen.")
        return

    selected_text = TEXTS[choice - 1]
    words = [word.strip(".,!?") for word in selected_text.split()]

    # Statistická analýza
    word_count = len(words)
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    numeric_count = sum(1 for word in words if word.isdigit())
    numeric_sum = sum(int(word) for word in words if word.isdigit())

    # Výstup
    print("\n--- ANALÝZA TEXTU ---")
    print(f"Počet slov: {word_count}")
    print(f"Počet slov začínajících velkým písmenem: {titlecase_count}")
    print(f"Počet slov psaných velkými písmeny: {uppercase_count}")
    print(f"Počet slov psaných malými písmeny: {lowercase_count}")
    print(f"Počet čísel: {numeric_count}")
    print(f"Součet všech čísel: {numeric_sum}")