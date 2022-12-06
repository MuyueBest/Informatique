#exo 1
d_pu = {"Épée en mousse":5, "Masque Dark Vador":30, "Hand spinner 3d":10, "Console Minux":150,"Lego Footix":15}
d_stock = {"Épée en mousse":10, "Masque Dark Vador":4, "Hand spinner 3d":10, "Console Minux":2,"Lego Footix":5}

for cle, valeur in d_stocks.items():
	if valeur <= 2:
		print(f"il faut remplir le stock de {cle}")

#exo 2
def verification(d1, d2):
	for i in d1.keys():
		if i not in d2:
			return False
	for j in d2.keys():
        if j not in d1:
            return False
    return True


assert verification(d_pu, d_stock) == True
del d_pu["Lego Footix"]
assert verification(d_pu,  d_stock) == False

#exo 3
def achat_possible(k ,v, d):
	""" truc """
      if k in d:
            return d[k] >= v
      return False

assert achat_possible("Hand spinner 3d", 2, d_stock) == True
assert achat_possible("Console Minux", 5, d_stock) == False
assert achat_possible(1 , 1, {}) == False
assert achat_possible("Hand spinner 3d" , 2, d_stock) == True

#exo 4
def achats_possibles(d_achats, d):
	""" truc """
    for k, v in d_achats.items():
        r = achat_possible(k ,v, d)
        if not r:
            return r
    return True

assert achats_possibles({"Hand spinner 3d": 2, "Console Minux": 5}, d_stock) == False
assert achats_possibles({"Hand spinner 3d": 2}, d_stock) == True
d_achats = {"Hand spinner 3d": 2, "Console Minux": 5}
assert achats_possibles(d_achats, d_stock) == False

#exo4(bonus)

def achats(d_achats, d_pu, d_stocks, facture=True):
	""" truc """
    total = 0
    for k, v in d_achats.items():
        r = achat_possible(k ,v, d_stocks)
        if r:
            d_stocks[k] = d_stocks[k] - v
            if facture:
                total = total + v * d_pu[k]
                print(f"{k}: {v} x {d_pu[k]} = {v * d_pu[k]}")
    if facture:
        print("-"*20)
        print(f"Prix total: {total}")


achats({"Hand spinner 3d": 2, "Lego Footix": 1}, d_pu, d_stock, True)
assert d_stock == {'Épée en mousse': 10, 'Masque Dark Vador': 4, 'Hand spinner 3d': 8, 'Console Minux': 2, 'Lego Footix': 4}