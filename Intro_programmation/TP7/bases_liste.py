##exo1
L = [5, 6, 7, 3, 1]
print(f"Premier élément de L {L[0]}.");print(f"Dernier élément de L {L[-1]}.")
L[1] = 0;L[3] = L[2]+L[4]
print(f"La liste L est {L}.")
var_aux = L[0];L[0] = L[1];L[1] = var_aux
print(f"La liste L est {L}.")
L[1], L[0] = L[0], L[1]
print(f"La liste L est {L}.")
L.remove(0)