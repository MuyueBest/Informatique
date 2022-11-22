##exo2
import random

R = [random.randint(1, 20) for i in range(10)]

R_append = []
for i in range(10):
	R_append.append(random.randint(1, 20))
	
long = len(R)

for i in range(long):
	print(R[i], end=' : ')
print()

for elt in R:
	print(elt, end=' : ')
print("\n")

total = 0
for elt in R:
	total += elt

nb_max = 0, 0
for i in range(long):
	if R[i] > nb_max[0]:
		nb_max = R[i], i
print(f"nb_max = {nb_max}")

nb_elt = 0
for elt in R:
	if elt >= 10:
		nb_elt += 1
print(f"nb_elt = {nb_elt}")

R2 = [R[i] if R[i] <= 10 else -R[i] for i in range(long)]
print(f"R2 = {R2}")

R3 = R+R2
print(f"R3 = {R3}")