# dans le fichier main.py

from fonctions import est_pair, jeu_devinette_nombre

# Test de la fonction est_pair
nombre_test = 17
print(f"Le nombre {nombre_test} est {'pair' if est_pair(nombre_test) else 'impair'}.")
print("hi")

# Lancer le jeu de devinette de nombre
jeu_devinette_nombre()
