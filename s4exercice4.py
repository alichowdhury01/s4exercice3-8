#Exercice 4:
#Écrire un programme avec une fonction prenant 2 floats et retournant leur addition soustraction et division. 
#Les résultats des additions doivent avoir au plus 1 chiffre après la virgule, 
#la soustraction 2 chiffres après la virgule et 
#la division 3 chiffres après la virgule.

from __future__ import division


def calculatrice(nb1, nb2):
    adition = (nb1) + (nb1)
    soustraction = (nb1) - (nb2)
    division = (nb1) / (nb2)
    return adition, soustraction, division
add, sous, div = calculatrice(2, 3)
print(f"addition: {add:.1f} soustraction: {sous:.2f} division: {div:.3f}")