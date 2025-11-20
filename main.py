"""
Module de vérification de palindromes.

Ce script permet de vérifier si une chaîne de caractères est un palindrome,
en ignorant la casse, les accents et la ponctuation.
"""

import unicodedata


#### Fonction secondaire

def ispalindrome(p: str) -> bool:
    """
    Vérifie si la chaîne p est un palindrome.

    Args:
        p (str): La chaîne à tester.

    Returns:
        bool: True si p est un palindrome, False sinon.
    """
    p_normalized = unicodedata.normalize('NFD', p)
    clean_chars = [
        c.lower() for c in p_normalized
        if not unicodedata.combining(c) and c.isalnum()
    ]
    clean_p = "".join(clean_chars)
    # Comparaison de la chaîne avec son inverse (slicing)
    return clean_p == clean_p[::-1]


#### Fonction principale

def main() -> None:
    """
    Fonction principale.
    Exécute une série de tests sur la fonction ispalindrome
    avec des chaînes prédéfinies.
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
