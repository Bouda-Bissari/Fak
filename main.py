# dans le fichier main.py

from fonctions import est_pair, jeu_devinette_nombre
from fonctions import est_premier

# Test de la fonction est_pair
nombre_test = 17
print(f"Le nombre {nombre_test} est {'pair' if est_pair(nombre_test) else 'impair'}.")

# Lancer le jeu de devinette de nombre
jeu_devinette_nombre()

# dans le fichier main.py



# Test de la fonction est_premier
nombre_test = 17
if est_premier(nombre_test):
    print(f"Le nombre {nombre_test} est premier.")
else:
    print(f"Le nombre {nombre_test} n'est pas premier.")
