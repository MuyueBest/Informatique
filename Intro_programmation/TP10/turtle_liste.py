from turtle import *

#exo 1
def rect(l:float, h:float, x=0, y=0):
	"""Trace un rectangle de longueur l et hauteur h depuis la position x et y."""
	penup()
	setposition(x, y)
	pendown()
	for _ in range(2):
		forward(l)
		left(90)
		forward(h)
		left(90)

#rect(50, 100, 10, 50)

#exo 2
#rect(50, 100, 0, 50)
#rect(50, 20, 50, 50)
#rect(50, 80, 100, 50)

#exo 3

color("blue")
		
def histo(liste:list, l:float, x:float, y:float):
	for i in range(1, len(liste)+1):
		if liste[i-1] >= 400:
			print(f"La {i} hauteur de la liste est trop grande.")
		else:
			rect(l, liste[i-1], x, y)
			x = x + l

histo([100, 50, 120, 12, -30, 60, 250, 100], 50, -10, 0)