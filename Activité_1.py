# Activité 1
# Objectif général : Utiliser le chiffre de César

# La liste réference pour notre alphabet
Alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 1) 
# Objectif : 
# Programmer une fonction qui renvoie le caractere de l'alphabet situé k rang apres, avec un modulo 26   

def chiffre_cesar_caractere(car, k) :
    # Trouve l'index du caractere dans l'alphabet
    i = Alphabet.index(car)
    # Décale de k positions avec un modulo 26 pour correspondre a l'alphabet
    j = (i + k)%26
    # Recupere la nouvelle lettre 
    nouvelle_lettre = Alphabet[j]
    return nouvelle_lettre
# Exemple avec Z pour le caractere et 4 pour k :
resultat = chiffre_cesar_caractere("Z", 4)
print(resultat) # Affiche D

# 2) 
# Objectifs : 
#Programmer une fonction qui renvoie une phrase codée par un décalage de César k 
#Si un caractere n'est pas présent dns l'alphabet, le laissez tel quel            
def chiffre_cesar_phrase(phrase, k):
    nouveau_texte = ""
    for car in phrase:
        # Verifie si le caractere est dans l'alphabet 
        if car not in Alphabet:
            # Laisse le caractere tel quel si il n'est pas dans l'alphabet
            nouveau_texte += car 
        else:
            # Utilise la fonction chiffre_cesar_caractere si celui ci est dans l'alphabet
            nouvelle_lettre_phrase = chiffre_cesar_caractere(car, k)
            # Ajoute le caractere afin de former une phrase 
            nouveau_texte += nouvelle_lettre_phrase
    return nouveau_texte
# Exemple avec la phrase "CAPTUREZ IDEFIX !" et 3 pour k :   
resultat = chiffre_cesar_phrase("CAPTUREZ IDEFIX !", 3)
print(resultat) # Affiche FDSWXUHC LGHILA ! 

# 3)
# Objectif :
# Programmer une fonction pour déchiffrer un texte grace au chiffre de César 

def dechiffre_cesar_phrase(phrase, k) :
    nouveau_texte = ""
    for car in phrase :
        if car not in Alphabet:
            nouveau_texte += car 
        else:
            nouvelle_lettre_phrase = chiffre_cesar_caractere(car, k)
            nouveau_texte += nouvelle_lettre_phrase
    return nouveau_texte
# Exemple avec la phrase "FDSWXUHC LGHILA !" et -3 pour k
# Afin de déchiffrer, j'ai choisi d'utiliser un décalage -k plutot que k sur une meme base de fonction 
resultat = dechiffre_cesar_phrase("FDSWXUHC LGHILA !", -3)
print(resultat) # Affiche "CAPTUREZ IDEFIX !"
