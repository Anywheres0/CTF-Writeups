import numpy as np
import galois

GF = galois.GF(2)

with open('gatevalues.txt', 'r') as file:
    binary_values = [line.strip() for line in file]

initialmatrix = [[GF(int(binary_values[element][row])) for element in range(616)] for row in range(616)]
col_removed = [row[1:] for row in initialmatrix]
row_removed = col_removed[1:]
matrix = np.array(row_removed)

### MATRIX INITIALIZED ###

with open('default.txt', 'r') as goal:
    default = goal.read()
    intended = default.replace("1", "a").replace("0", "1").replace("a", "0")
    intended = intended[1:]

solutions = np.array([GF(int(char)) for char in intended])

solved_matrix = np.linalg.solve(GF(matrix), GF(solutions))


flagtext = bytes.fromhex(str(hex(int("".join(str(row) for row in solved_matrix),2)))[2:]).decode()

print("FLAG: amateursCTF{" + flagtext + "}")