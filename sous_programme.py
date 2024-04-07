"""LES SOUS PROGRAMMES: c'est le fait de découper notre code en fragment"""
"""
    On distingue deux types de sous-programmes
        -->Procedures: Elle ne renvoie de pas de valeurs, ça peut juste une modfication à faire, ça peut etre un affichage
        -->Fonctions: Qui renvoie une valeur
    
    
    """

def perimetre_du_rectangle(largeur:float,longueur:float)->float:
    resultat:float=(largeur+longueur)*2
    return resultat

def demi_perimetre1(perimettre:float)->float:
    resultat=perimettre/2
    return resultat
    
def demi_perimetre2(largeur:float,longueur:float)->float:
    resultat=perimetre_du_rectangle(largeur,longueur)/2
    return resultat
    

def surface_du_rectangle(largeur:float,longueur:float)->float:
    resultat=longueur*largeur
    return resultat

def affichage_caracteristique_rectangle(longueur,largeur):
    print("la largeur est de {} \nla longueur est de {}".format(largeur,longueur))
    print("le perimettre est de {}".format(demi_perimetre2(longueur,largeur)))
    print("le demi perimettre est de {}".format(perimetre_du_rectangle(longueur,largeur)))
    print("la surface est {}".format(surface_du_rectangle(longueur,largeur)))

affichage_caracteristique_rectangle(5,6)
affichage_caracteristique_rectangle(4,6)
affichage_caracteristique_rectangle(2,6)
affichage_caracteristique_rectangle(1,6)
affichage_caracteristique_rectangle(0,6)
