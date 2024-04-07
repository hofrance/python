from math import sqrt

# Calcul du périmètre d'un triangle
# Cette fonction prend en arguments les longueurs des trois côtés d'un triangle
# et retourne le périmètre.
def perimetre_triangle(a: float, b: float, c: float) -> float:
    return a + b + c

# Calcul de la surface d'un triangle en utilisant la formule de Héron
# La fonction prend en arguments les longueurs des trois côtés d'un triangle
# et retourne la surface calculée avec la formule de Héron.
def surface_triangle_heron(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2  # Demi-périmètre du triangle
    return sqrt(p * (p - a) * (p - b) * (p - c))

# Détermination si un triangle est équilatéral
# La fonction retourne True si toutes les longueurs des côtés sont égales, False sinon.
def is_equilateral_triangle(a: float, b: float, c: float) -> bool:
    return a == b == c

# Détermination si un triangle est isocèle
# Un triangle est isocèle si au moins deux côtés ont la même longueur.
# La fonction retourne True si c'est le cas, False sinon.
def is_isocele_triangle(a: float, b: float, c: float) -> bool:
    return a == b or a == c or b == c

# Détermination si un triangle est quelconque
# Un triangle est quelconque s'il n'est ni équilatéral ni isocèle.
# La fonction retourne True si c'est le cas, False sinon.
def is_quelconque_triangle(a: float, b: float, c: float) -> bool:
    return not is_equilateral_triangle(a, b, c) and not is_isocele_triangle(a, b, c)

# Affichage des caractéristiques d'un triangle
# Cette fonction affiche le périmètre et la surface d'un triangle,
# ainsi que son type (équilatéral, isocèle, quelconque).
def affiche_caracteristique_triangle(a, b, c):
    print(f"Le périmètre est {perimetre_triangle(a, b, c)}")
    print(f"La surface est {surface_triangle_heron(a, b, c)}")
   
    if is_equilateral_triangle(a, b, c):
        print("Le triangle est équilatéral")
    elif is_isocele_triangle(a, b, c):
        print("Le triangle est isocèle")
    else:  
        print("Le triangle est quelconque")

# Exemple d'utilisation de la fonction affiche_caracteristique_triangle
affiche_caracteristique_triangle(3, 5, 4)
