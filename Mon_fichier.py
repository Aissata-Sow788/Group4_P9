# Écrire un algorithme qui demande 10 nombres à l'utilisateur.
# Calculer et afficher la somme et la moyenne de tous les éléments.
nombres = []
somme = 0 
moyenne = 0
taille = 10
for i in range(taille) :
    nombres.append( float(input(f"Veuillez saisir le nombre {i+1}")))
    somme += nombres[i]
moyenne = somme / taille
print(f"La somme des nombres vaut : {somme}")
print(f"La moyenne des nombres vaut : {moyenne}")
