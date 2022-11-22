#exo 1
with open('emails.txt') as f:
	M = f.read().splitlines()
print(M)

#exo 2
print(f"M contient {len(M)} adresses")

#exo 3
adresse_long = str()
for adresse in M:
	if len(adresse) > len(adresse_long):
		adresse_long = adresse
print(f"L'adresse la plus longue est {adresse_long}")

#exo 4
D = [adresse.split("@")[-1] for adresse in M]
print(D)

#exo 5
Du = list()
for adresse in M:
	if adresse.split("@")[-1] not in Du:
		Du.append(adresse.split("@")[-1])
print(Du)

#exo 6
user_par_domaine = [[domaine, 0] for domaine in Du]
for user in D:
	for i in range(len(Du)):
		if Du[i] in user:
			user_par_domaine[i][1] += 1
print(user_par_domaine)

#exo 7
liste_tuple = list()
for liste in user_par_domaine:
	liste_tuple.append((liste[0], liste[1]))
print(liste_tuple)

#exo bonus
nb_fr = 0
for adresse in D:
	if '.fr' in adresse:
		nb_fr += 1
print(nb_fr)