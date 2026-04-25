import pulp as pl
import os

def max_matrix_sum(matrix):
    #-------------Inicializálás-------------
    rows = len(matrix)
    cols = len(matrix[0])
    # Változók
    x = pl.LpVariable.dicts("x", (range(rows), range(cols)), cat="Binary")

    model = pl.LpProblem("Max_Matrix_Sum", pl.LpMaximize)

    #---------------Feltételek---------------
    # Minden sorban és oszlopban legfeljebb egy elem lehet
    for i in range(rows):
        model += sum(x[i][j] for j in range(cols)) <= 1
    for j in range(cols):
        model += sum(x[i][j] for i in range(rows)) <= 1

    # Célfüggvény
    model += sum(matrix[i][j] * x[i][j] for i in range(rows) for j in range(cols))

    
    model.solve(pl.PULP_CBC_CMD(msg=0))
    max_sum = pl.value(model.objective)
    return max_sum


base = os.path.dirname(__file__)
path = os.path.join(base, "pr_euler_345.txt")
with open(path) as f:
    lines = f.read().strip().split("\n")
    matrix = []
    for line in lines:
        row = list(map(int, line.split()))
        matrix.append(row)

result = max_matrix_sum(matrix)
print(result)