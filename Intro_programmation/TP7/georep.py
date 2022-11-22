##exo3
import turtle
from turtle import *
import math
fois = 0
while fois < 4:
	forward(100)
	right(90)
	fois += 1

n = int(input("Nombre côtés : "))
for i in range(n):
	forward(80)
	right(360/n)

max = int(input("Donnez le max : "))
m = 0
for j in range(91, 180):
	for i in range(0, max):
		if (i*360)%j == 0:
			m = j
print(j)

first_x = xcor()
first_y = ycor()
x = -1000
y = -1000
position_toute = [(first_x, first_y)]

while not math.isclose(first_x, x, abs_tol=1e-8) and not math.isclose(first_x, x, abs_tol=1e-8):
	turtle.speed(10)
	forward(100)
	right(m)
	x = xcor()
	y = ycor()
	position_toute.append((x, y))

print(position_toute, position_toute[0], position_toute[-1])