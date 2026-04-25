import pulp as pl
import os


def number_mind(num_of_digits, conditions):
    #conditions = [tipp stringként, helyes számjegyek száma]
    #-------------Inicializálás-------------
    n = num_of_digits
    digits = range(10)
    # Változók
    x = pl.LpVariable.dicts("x", (range(n), digits), cat="Binary")

    model = pl.LpProblem("Number_Mind", pl.LpMinimize)

    #Mindegy számjegy helyére egy szám
    for i in range(n):
        model += sum(x[i][d] for d in digits) == 1

    #Kapott tipp-feltételek
    for tipp, k in conditions:
        model += sum(x[i][int(tipp[i])] for i in range(n)) == k

    # megoldás
    model.solve(pl.PULP_CBC_CMD(msg=0))
    solution = []
    for i in range(n):
        for d in digits:
            if pl.value(x[i][d]) == 1:
                solution.append(str(d))

    return "".join(solution)

pelda_1 = [
    ("90342", 2),
    ("70794", 0),
    ("39458", 2),
    ("34109", 1),
    ("51545", 2),
    ("12531", 1)]

print(number_mind(5, pelda_1))

base = os.path.dirname(__file__)
path = os.path.join(base, "project_euler_185.txt")
with open(path) as f:
    lines = f.read().strip().split("\n")
    pelda_2 = []
    for line in lines[1:]:
        tipp, k = line.split(";")
        pelda_2.append((tipp, int(k[0])))

print(number_mind(16, pelda_2))
