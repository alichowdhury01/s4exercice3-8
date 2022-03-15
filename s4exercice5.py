#Exercice 5:
#Écrire un programme prenant l'année de naissance de l'utilisateur et lui retournant sa génération. 
#Vous pouvez utiliser la source suivante: https://www.eurecia.com/blog/generations-x-y-z-sont-elles/

def gen():

    annee = int(input("Veuillez entrer votre année de naissance: "))
    
    if 1946 <= annee <= 1964:
        print("Vous fêtes parti de la génération des Baby-boomers")
    elif 1965 <= annee <= 1979:
        print("Vous fêtes parti de la génération X")
    elif 1980 <= annee <= 1999:
        print("Vous fêtes parti de la génération Y")
    elif annee >= 2000:
        print("Vous fêtes parti de la génération Z")
    else:
        print("T'es trop vieux ou vieille!")
    return

gen()