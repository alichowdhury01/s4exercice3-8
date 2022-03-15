#Exercice 3:
#Écrire un programme offrant un menu à un utilisateur avec 3 choix et lui affichant la phrase suivante une fois sélectionné:
#1. Bonjour
#2. Au revoir
#3. À plus tard

#Fonction selection:
def selection():

    #Input pour la valeur choix:
    choix = int(input("Veuillez faire votre sélection\n 1 pour Bonjour\n 2 pour Au revoir\n 3 pour À plus tard: "))

    #Condition du input fait:
    if choix == 1:
        print("Bonjour")
    elif choix == 2:
        print("Au revoir")
    elif choix == 3:
        print("À plus tard")
    else:
        print("Choix invalide")
    return

#Execution de la fonction selection:
selection()