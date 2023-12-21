# dans le fichier fonctions.py

import random

# Fonction pour le jeu de devinette de nombre
def jeu_devinette_nombre():
    nombre_secret = random.randint(1, 100)
    essais = 0

    print("Bienvenue dans le jeu de devinette de nombre!")
    
    while True:
        proposition = int(input("Devinez le nombre entre 1 et 100 : "))
        essais += 1

        if proposition == nombre_secret:
            print(f"Félicitations! Vous avez deviné le nombre en {essais} essais.")
            break
        elif proposition < nombre_secret:
            print("Le nombre est plus grand. Essayez à nouveau.")
        else:
            print("Le nombre est plus petit. Essayez à nouveau.")

# Fonction pour vérifier la parité d'un nombre
def est_pair(nombre):
    return nombre % 2 == 0

# Tests
if __name__ == "__main__":
    nombre_test = 17
    print(f"Le nombre {nombre_test} est {'pair' if est_pair(nombre_test) else 'impair'}.")
    
    # Lancer le jeu de devinette de nombre
    jeu_devinette_nombre()
