import numpy as np
import os

matrix_2 = []
matrix_1 = np.array([[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111],
                     [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]])


file = os.path.join(os.path.dirname(__file__), '0083_matrix.txt')
with open(file) as f:
    for line in f:
        lline = [int(x) for x in line.strip().split(',')]
        matrix_2.append(lline)
    matrix_2 = np.array(matrix_2)


def dijsktra(matrix):
    meret = len(matrix)
    nem_latogatott = [(sor, oszlop) for sor in range(meret) for oszlop in range(meret)]
    vegtelen = matrix.sum() + 1
    d = np.full((meret, meret), vegtelen)
    d[0][0] = matrix[0][0]
    while (meret-1, meret-1) in nem_latogatott:
        legkisebb = min(nem_latogatott, key=lambda pont: d[pont])
        m_sor, m_oszlop = legkisebb
        fel = (m_sor - 1, m_oszlop)
        le = (m_sor + 1, m_oszlop)
        jobb = (m_sor, m_oszlop + 1)
        bal = (m_sor, m_oszlop - 1)
        szomszedok = [fel, le, jobb, bal]
        ig_szomszedok = [szomszed for szomszed in szomszedok if szomszed in nem_latogatott]
        for ig_szomszed in ig_szomszedok:
            sz_sor, sz_oszlop = ig_szomszed
            if d[m_sor][m_oszlop] + matrix[sz_sor][sz_oszlop] < d[sz_sor][sz_oszlop]:
                d[sz_sor][sz_oszlop] = d[m_sor][m_oszlop] + matrix[sz_sor][sz_oszlop]
        nem_latogatott.remove(legkisebb)

    return d[-1][-1]


print(dijsktra(matrix_1))
print(dijsktra(matrix_2))
