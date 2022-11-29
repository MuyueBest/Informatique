#exo 1
Daugustin = {"Nom":"ROUX", "Prenom":"Augustin"}
Daxel = {"Nom":"JOUVELLIER", "Prenom":"Axel"}

#exo 2
Daugustin["Age"] = 17
Daxel["Age"] = 19
print(Daugustin, Daxel)

#exo 3
print("\n")
print(f'12<17 : {len(Daugustin["Nom"]+Daugustin["Prenom"]) < Daugustin["Age"]}')
print(f'14<19 : {len(Daxel["Nom"]+Daxel["Prenom"]) < Daxel["Age"]}')

#exo 4
D2augustin = {"Couleur":"Rose", "Orientation Sexuel":"Ni homme, ni femme, c'est hurleur", "Fidele":"Oui I love 02"}
Daugustin.update(D2augustin)
D2axel = {"Couleur pref":"Orange", "Sex":"Homme"}
Daxel.update(D2axel)

#exo 5
del Daugustin["Age"]
Daugustin["AgeLycee"] = "15-17"
del Daxel["Age"]
Daxel["AgeLycee"] = "17-19"

#exo 6
print("\n")
for cle, valeur in Daugustin.items():
	print(cle, valeur)
print("\n")
for cle, valeur in Daxel.items():
	print(cle, valeur)