import random
from tkinter.messagebox import NO

NOMBRE_A_TROUVER = 5

nombre_propose = int(input("Entre un nombre s'il vous plait: "))

while nombre_propose != NOMBRE_A_TROUVER:
    if nombre_propose > NOMBRE_A_TROUVER:
        print("c'est moins")
    elif nombre_propose < NOMBRE_A_TROUVER:
        print("c'est plus")
    else:
        break
    nombre_propose = int(input("Entre un nombre s'il vous plait: "))

    # demande un nombre à l'utilisateur
    # indique si c'est plus ou moins
    # indique si c'est gagné

print("bravo")
