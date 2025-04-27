"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Matej Kaplan
email: kaplan.matej1@seznam.cz
"""
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

def login():
    username = input("Zadejte přihlašovací jméno: ")
    password = input("Zadejte heslo: ")