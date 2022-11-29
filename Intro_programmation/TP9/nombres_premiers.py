import time, random

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
end = time.time()
temps1 = end - start
print(f"Nombres premier méthode 1: {P}")
print(f"Temps d'exécution de la méthode 1: {temps1:.2}ms\n")

#exo 3
print(f"Il y a {len(P)} nombres premier\n")

#Méthode 2
#exo 1
start = time.time()
def is_prime2(n:int)->bool:
	"""Renvoie True si n est un entier, False sinon"""
	for i in range(2, n):
		if (n%i) == 0:
			return False
	return True
print(is_prime2(1000))
end = time.time()
temps2 = end - start
#
print(f"Temps d'exécution de la méthode 2: {temps2:.2}ms\n")

#exo 2
print(f"La méthode 1 est executer en {temps1:.2}ms et la méthode 2 en {temps2:.2}ms, la méthode 2 est donc la plus rapide.\n")

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
temps3 = end - start
print(f"Temps d'exécution de la méthode 3: {temps3:.2}ms\n")

#exo 2
print("Oui c'est plus lent, parceque au lieu de faire une itération avec la liste P, nous faisons une itération de chaque multiple de chaque éléments de P.\n")
#	1000
#	 ∑ P^P-i  =  nombres d'itération
#	i=2





#Exercice 4 TP9
#exo 3
def testPrimalisteFermat(N):
	a = random.randint(0, N-1)
	if a**(N-1)%N == 1:
		return True
	else:
		return False

#exo 4
erreur = 0
nombre_nb_premier = 0
for i in range(2, 10000):
	verif = is_prime2(i)
	if not(testPrimalisteFermat(i)) == verif:
		erreur += 1
	if verif:
		nombre_nb_premier += 1
		
print(erreur, nombre_nb_premier)