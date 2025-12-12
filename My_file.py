#Ecrire un algorithme qui permet de calculer le factoriel d’un nombre
while True:
    nombre = input("veuillez saisir un nombre positif : ")
    if not nombre.isnumeric :
        print("Erreur!!! Le nombre doit etre positif!!!")
    else :
        nombre = int(nombre)
        if nombre < 0 :
            print("Erreur!!! Le nombre doit etre positif!!!")
        else : 
            break
        
fact = 1
if nombre == 0 : 
    print(f"Le factoriel de {nombre} vaut : {fact}")
else:
    for i in range(1,nombre + 1):
        fact = fact *i

print(f"Le factoriel de {nombre} vaut : {fact}")
def Factoriel(nombre) :
    fact = 1
    if nombre == 0 : 
        print(f"Le factoriel de {nombre} vaut : {fact}")
    else:
        for i in range(1,nombre + 1):
            fact = fact *i
    return fact

while True:
    nombre = input("veuillez saisir un nombre positif : ")
    if not nombre.isnumeric :
        print("Erreur!!! Le nombre doit etre positif!!!")
    else :
        nombre = int(nombre)
        if nombre < 0 :
            print("Erreur!!! Le nombre doit etre positif!!!")
        else : 
            break

fact = Factoriel(nombre)
print(f"Le factoriel de {nombre} vaut : {fact}")
