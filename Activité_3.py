# Activité 3 
# Objectif général : Utiliser la fréquence d'apparition des lettres pour déchiffrer un message en essayant de deviner la substitution 

# La liste servant de référence pour notre alphabet :
Alphabet = "abcdefghijklmnopqrstuvwxyz"

# 1)
# Objectif :
# Programmer une fonction qui réalise une substitution de lettres basée sur deux alphabets
# Elle remplace nos lettres de départ par les lettres connues de notre alphabet d'arrivée

# On initialise un alphabet de départ, basé sur notre alphabet
Alphabet_depart = "abcdefghijklmnopqrstuvwxyz"
# On initialise un alphabet d'arrivé (donné dans l'énoncé)
Alphabet_arrivee = "...S.....E..T............."

def substitution(phrase, Alphabet_depart, Alphabet_arrivee) :
    # On initialise une nouvelle chaine vide pour notre nouvelle phrase
    nouvelle_phrase = ""
    for car in phrase : 
        # On verifie que notre caractere est dans notre alphabet de départ
        if car not in Alphabet_depart :
            # Si non, on l'ajoute tel quel
            nouvelle_phrase += car 
        else :
            # Si oui, on trouve l'index du caractere dans cet alphabet 
            i = Alphabet_depart.index(car)
            # On ajoute a la nouvelle phrase le caractere correspondant a l'index dans l'alphabet d'arrivee 
            nouvelle_phrase += Alphabet_arrivee[i]  
    return nouvelle_phrase
# Exemple avec la phrase "jdolwt jd tm vb ?" et nos deux alphabets selectionnés
resultat = substitution("jdolwt jd tm vb ?", Alphabet_depart, Alphabet_arrivee)
print(resultat) #Affiche "ES.... ES .T .. ?"
# Erreur de l'énoncé :
# Dans l'énoncé il est écrit qu'en utilisant la phrase "jdolwt jd tm vb ?" nous obtiendrons "ES...T ES T. .. ?"
# Afin de deviner "Esprit es tu la ?" mais le resultat est bien : ES.... ES .T .. ?

# 2) 
# Objectifs :
# Programmer une fonction qui clcule et renvoie le nombre d'appartitions des lettres dans une phrase sous forme de liste
# On ne tiens pas compte des caracteres autre que les lettres minuscules 
# Programmer une seconde fonction dans le but d'afficher proprement les lettres qui apparaissent et leur nombre d'apparition

# Analyse la fréquence d'apparition d'une lettre dans une phrase 
def statistique(phrase) :
    # Initialise une liste composée de 26 zéros
    liste_nombre = [0] * 26
    # Parcours chaque caractere de la phrase
    for car in phrase :
        # Verifie si le caractere est dans notre alphabet
        if car in Alphabet :   
            # Cherche l'index du caractere au sein de notre alphabet
            i = Alphabet.index(car)
            # Ajoute 1 dans notre liste a l'emplacement correspondant a l'index de notre alphabet
            liste_nombre[i] +=1
    return liste_nombre 
# Exemple avec la phrase "j'adore le soleil"    
resultat = statistique("j'adore le soleil")
print(resultat) # Affiche [1, 0, 0, 1, 3, 0, 0, 0, 1, 1, 0, 3, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,]

# Affiche proprement le resultat de notre fonction précedente en associant chaque lettre a son nombre 
def affiche_statistique(phrase) :
    # Recupere le resultat de la fonction statistique et l'enregistre sous "brouillon"
    brouillon = statistique(phrase)
    # Parcours brouillon 
    for i in range(len(brouillon)) :
        # Recupere le nombre d'apparition selon l'emplacement du caractere au sein de brouillon  
        apparition = brouillon[i]
        # Cherche la lettre correspondante au sein de notre alphabet
        lettre = Alphabet[i]
        # Ecrit et associe chaque lettre a son nombre d'apparition
        print(lettre, ":", apparition)
# Exemple avec la phrase j'adore le soleil  
resultat = affiche_statistique("j'adore le soleil")
print(resultat)  
# Affiche sous forme de colones : a : 1 , b : 0, c : 0, d : 1, e : 3....

# 3) 
# Objectif : 
# Programmer une fonction en modifiant nos fonctions de statistiques pour avoir une fonction qui calcule la fréquence d'apparition d'une lettre dans une phrase (%)
# Et une autre fonction dédiée a l'affichage propre de la fonction de calcul 

# Fonction calculant la fréquence d'apparition d'une lettre dans une phrase en pourcentage
def frequence(phrase) :
    # Initialise une liste composée de 26 zéros
    liste_nombre = [0] * 26
    # Initialise une variable qui compte de le nombre total de lettre dans la phrase
    total_lettre = 0
    # Initialise une liste vide qui va contenir les fréquences en %
    frequence = []
    # Parcours tous les caracteres de la phrase
    for car in phrase :
        # Verifie si le caractere est dans l'alphabet
        if car in Alphabet :
            # Recupere la position de la lettre dns l'alphabet
            i = Alphabet.index(car)
            # Ajoute 1 au compteur correspondant a la lettre 
            liste_nombre[i] +=1
            # Ajoute 1 au total des lettres prises en compte
            total_lettre +=1
    # On parcours le nombre d'apparition de chaque lettre dans notre liste        
    for nombre_app in liste_nombre : 
        # Calcule la fréquence et ajoute le resultat a notre liste "fréquence"
        frequence.append((nombre_app/total_lettre)*100) 
    return frequence 
# Exemple avec la phrase "j'adore le soleil
resultat = frequence("j'adore le soleil")
print(resultat) # Affiche [7.142857142857142, 0.0, 0.0,...]

# Fonction programmée pour rendre le resultat de notre fonction précedente plus lisible et compréhensible 
def affiche_frequence(phrase) : 
    # Initialise un brouillon pour stocker le resultat de ma fonction frequence
    brouillon = frequence(phrase)
    # Parcours ce brouillon indice par indice 26 fois pour obtenir une valeur par lettre
    for i in range(len(brouillon)) :
        # Recupere la frequence associée a la lettre 
        place = brouillon[i]
        # Recupere la lettre correspondante dans l'alphabet
        lettre = Alphabet[i]
        # Affiche le resultat en associant chaque lettre a sa frequence 
        print(lettre, ":", place)
# Exemple avec la phrase "j'adore le soleil"
resultat = affiche_frequence("j'adore le soleil")
print(resultat) # Affiche en colone : a : 7.142857142857142 , b : 0.0 , c : 0.0 etc. 
