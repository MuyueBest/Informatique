import time

#Méthode 1
#exo 1
def is_prime(n:int)->bool:
	"""Renvoie True si n est un entier, False sinon"""
	for i in range(2, n):
		if (n%i) == 0:
			return False
	return True
print(f"97 : {is_prime(97)}\n")

#exo 2
start = time.time()
P = list()
for x in range(2, 1000):
	if is_prime(x) == True:
		P.append(x)
print(f"Nombres premier : {P}")
end = time.time()
elapsed1 = end - start
print(f"Temps d'exécution de la méthode 1: {elapsed1:.2}ms\n")

#exo 3
print(f"Il y a {len(P)} nombres premier\n")

#Méthode 2
#exo 1
start = time.time()
def is_prime2(n:int)->bool:
	"""Renvoie True si n est un entier, False sinon"""
	for i in range(2, P):
		if (n%i) == 0:
			return False
	return True
end = time.time()
elapsed2 = end - start
print(f"Temps d'exécution de la méthode 2: {elapsed2:.2}ms\n")

#exo 2
print(f"La méthode 1 est executer en {elapsed1:.2}ms et la méthode 2 en {elapsed2:.2}ms, la méthode 2 est donc la plus rapide.\n")

#Méthode 3
#exo 1
start = time.time()
def nb_premier3(start:int, end:int)->list:
	"""Renvoie tous les nombres premiers entre start et end."""
	L = [nb for nb in range(start, end+1)]
	indice = 0
	nb = L[indice]
	while nb != L[-1]:
		for nbs in L:
			if nbs%nb == 0 and nb != nbs:
				L.remove(nbs)
		indice += 1
		nb = L[indice]
	return L
print(nb_premier3(2, 1000))
end = time.time()
elapsed3 = end - start
print(f"Temps d'exécution de la méthode 3: {elapsed3:.2}ms\n")

#exo 2
print("Oui c'est plus lent, parceque au lieu de faire une itération avec la liste P, nous faisons une itération de chaque multiple de chaque éléments de P.")
#	1000
#	 ∑ P^P-i  =  nombres d'itération
#	i=2