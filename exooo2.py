""" Exercice 5 : Recherche de doublons dans une liste (Boucle et Vérification) 
Demandez à l'utilisateur de saisir 7 nombres pour former une liste.
Vérifiez si cette liste contient au moins deux fois la même valeur c’est-a-dire un doublon.
Affichez :
"Doublons trouvés" si au moins une valeur est répétée.
"Aucun doublon" sinon.
 """

list=[]

print(f"donnez sept nombres")

for i in range(1,8):
    print(f"donnez l'element{i}")
    nbr=int(input())
    list.append(nbr)
    doublon=set((list))
if len(list) != len(doublon):
     print(f"Doublon trouve")
else:
    print(f"pas de doublon")
print(f"la liste des nombres est{list}")  
print(doublon)  

