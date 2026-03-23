# Activité 1
# Objectif : Utiliser le chiffre de César

# 1) 
def chiffre_cesar_caractere(car, k) :
    # Vérifie si le caractere se trouve dans l'alphabet 
    if car not in Alphabet :
            return car
    # Trouve l'index du caractere dns l'alphabet
    i = Alphabet.index(car)
    # Décale de k positions avec un modulo 26 pour correspondre a l'alphabet
    j = (i + k)%26
    # Recupere la nouvelle lettre 
    nouvelle_lettre = Alphabet[j]
    return nouvelle_lettre
# Exemple avec Z pour le caractere et 4 pour k :
resultat = chiffre_cesar_caractere("Z", 4)
print(resultat) # Affiche D
