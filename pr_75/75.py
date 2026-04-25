import pulp as pl

def solve_production(c, s, a, b):
    """
    p[i] - egységár
    s[i] - kezdeti költség
    a[j][i] - i-dik termékhez szükséges j-dik erőforrás 
    b[j] - kapacitás
    M[i] - felsőkorlátok
    """
    # ------------Inicializálás------------
    k = len(c)      
    m = len(b)
    
    # Felsőkorlátok meghatározása
    M = []
    for i in range(k):
        limits = []
        for j in range(m):
            if a[j][i] > 0:
                limits.append(b[j] / a[j][i])
        M.append(min(limits))
    model = pl.LpProblem("Termeles", pl.LpMaximize)
    
    # ----------Probléma felállítása----------
    # változók
    x = pl.LpVariable.dicts("x", range(k), cat="Binarary")
    y = pl.LpVariable.dicts("y", range(k), cat="Binary")

    # célfüggvény
    model += pl.lpSum(c[i]*x[i] - s[i]*y[i] for i in range(k))

    # feltételek
    for j in range(m):
        model += pl.lpSum(a[j][i]*x[i] for i in range(k)) <= b[j]
    for i in range(k):
        model += x[i] <= M[i]*y[i]
    status = model.solve()

    #----------Megoldás kiírása----------
    x_sol = [pl.value(x[i]) for i in range(k)]
    y_sol = [pl.value(y[i]) for i in range(k)]

    return x_sol, y_sol, pl.LpStatus[status]