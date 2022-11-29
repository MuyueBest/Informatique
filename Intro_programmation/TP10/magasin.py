#exo 1
d_pu = {"Épée en mousse":5, "Masque Dark Vador":30, "Hand spinner 3d":10, "Console Minux":150,"Lego Footix":15}
d_stock = {"Épée en mousse":10, "Masque Dark Vador":4, "Hand spinner 3d":10, "Console Minux":2,"Lego Footix":5}

#exo 2
def verification(d1:dict, d2:dict)->bool:
	"""Vérifie que deux dictionnaires ont exactement les mêmes clés."""
	cle_d1 = [cle for cle in d1.keys()]
	cle_d2 = [cle for cle in d2.keys()]
	
	for j in range(len(cle_d1)):
		if cle_d1[j] != cle_d2[j]:
				return False
	return True
	
assert verification(d_pu, d_stock) == True

#exo 3
def achat_possible(k:str, v:int, d:dict):
	"""Indique si l’on peut acheter le produit k en quantité v """
	if d[k] >= v:
		return True
	return False

assert achat_possible("Hand spinner 3d", 2, d_stock) == True
assert achat_possible("Console Minux", 5, d_stock) == False

#exo 4
def achats_possibles(k, v, d=None):
	"""Indique si l’on peut acheter le produit k en quantité v """
	if d != None:
		return achat_possible(k, v, d)
	else:
		liste_tuple = [tuple for tuple in k.items()]
		for tuple in liste_tuple:
			if tuple[1] > v[tuple[0]]:
				return False
		return True

assert achats_possibles({"Hand spinner 3d": 2}, d_stock) == True
d_achats = {"Hand spinner 3d": 2, "Console Minux": 5}
assert achats_possibles(d_achats, d_stock) == False
