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

rect(50, 100, 10, 50)