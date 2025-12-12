stock_initial = int(input("entrer un produit :"))
stock_vendue = int(input("entrez le nombre de produit vendus:"))

restant_produit = stock_initial - stock_vendue

print(f"le stock restant est : {restant_produit}")

if restant_produit < 10:
    print("Attention : stock faible, penser au réapprovisionnement.")
else :
    print("stock pleins")









    