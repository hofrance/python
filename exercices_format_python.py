
# Exercices sur la méthode .format() en Python


# Exercice 2: Utilisation des variables
prenom = "Richard"
age = 23
# Utilisez .format() pour afficher "Je m'appelle Richard et j'ai 23 ans."
print("Je m'appelle {} et j'ai {} ans.".format(prenom, age))

# Exercice 3: Ordre des arguments
# Utilisez .format() avec plus de deux arguments et affichez-les dans un ordre différent.
print("J'ai {1} ans et je m'appelle {0}.".format(prenom, age))

# Exercice 4: Nommer explicitement des arguments
# Nommez explicitement les arguments et utilisez-les.
print("Mon prénom est {name} et mon domaine est la {field}.".format(name=prenom, field="cybersécurité"))

# Exercice 5: Formatage des nombres
# Affichez le nombre 3.14159 avec deux décimales.
print("{:.2f}".format(3.14159))

# Exercice 6: Alignement et espacement
# Créez une chaîne de caractères alignée à gauche, une centrée, et une alignée à droite.
print("{:<10} | {:^10} | {:>10}".format("Gauche", "Centre", "Droite"))

# Exercice 7: Utilisation des dictionnaires
info = {'prenom': 'Richard', 'age': 23}
# Passez un dictionnaire à .format() et utilisez ses clés.
print("Je m'appelle {prenom} et j'ai {age} ans.".format(**info))

# Exercice 8: Formatage conditionnel
reussite = True
# Utilisez .format() pour conditionnellement afficher un message.
print("{0}".format("J'ai réussi l'examen!" if reussite else "Je dois retenter l'examen."))

# Exercice 9: Utilisation avec des listes
liste = ['Python', 'Java', 'C++']
# Passez une liste à .format() et utilisez l'indexation.
print("J'apprends {0[0]} et {0[1]}.".format(liste))

# Exercice 10: Chaînes multilignes et indentation
# Utilisez .format() avec une chaîne multilignes.
print('''
Nom: {0}
Âge: {1}
Domaine: {2}
'''.format(prenom, age, "Cybersécurité"))
