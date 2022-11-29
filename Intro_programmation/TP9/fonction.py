#exo 1
def aire_carre(cote:float)->float:
	"""Donne l'aire d'un carré de côte donné"""
	return cote**2

#exo 2
def aire_rectangle(longueur:float, largeur:float)->float:
	"""Donne l'aire d'un triangle de longueur et largeur donné"""
	return longueur*largeur

#exo 3
def aire_carre2(cote:float)->float:
	"""Donne l'aire d'un carré de côte donné"""
	return aire_rectangle(cote, cote)

#exo 4
def aire_rectangle2(longueur = None, largeur = None)->float:
	"""Donne l'aire d'un triangle de longueur et largeur donné"""
	if (longueur == largeur) or (largeur == None):
		if (longueur == None):
			return aire_carre(largeur)
		return aire_carre(longueur)
	return longueur*largeur

#exo 5
def coords_carre(c:int, coin_inf_gauche:tuple)->list:
	"""Renvoie tous les coordonnées des sommet d'un carré"""
	return [coin_inf_gauche, (coin_inf_gauche[0]+c, coin_inf_gauche[1]), (coin_inf_gauche[0]+c,coin_inf_gauche[1]+c), (coin_inf_gauche[0],coin_inf_gauche[1]+c)]