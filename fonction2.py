

def verifiermdp(mdp: str):
    
    mdp_vrai = "123a"
    x = 0

    while mdp != mdp_vrai and i < 3:
        mdp = input(f"incorrect veuiller saisir un mot de passe correct")
        print(f"tentative : {x}")
        x = x + 1

    return mdp == mdp_vrai

    
mdp_correct =(input(f"entrez un mots de passe :"))



if verifiermdp(mdp_correct):
    print("acces autoriser")
else:
    print("compte bloquer")