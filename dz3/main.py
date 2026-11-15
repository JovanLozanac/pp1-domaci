def ucitavanjeMatrice():
    linija = input().split()
    x = int(linija[0])
    y = int(linija[1])
    mat = []

    for i in range(x):
        linija = input().split()
        mat.append(linija)

    return mat

def pomeriDesno (mat, pomeraj):
    _mat = mat.copy()
    for k in range (pomeraj):
        for i in range (len(_mat)):
            for j in range(len(_mat[0]) - 1, 0, -1):
                _mat[i][j] = _mat[i][j-1]
                if (j == 1): _mat[i][0] = 'o'
    return _mat

def pomeriLevo (mat, pomeraj):
    _mat = mat.copy()
    for k in range(pomeraj):
        for i in range(len(_mat)):
            for j in range(0, len(_mat[0]) - 1):
                _mat[i][j] = _mat[i][j + 1]
                if (j == len(_mat[0]) - 2): _mat[i][len(_mat[0]) - 1] = 'o'
    return _mat
def pomeriDole (mat, pomeraj):
    _mat = mat.copy()
    for k in range(pomeraj):
        for j in range(len(_mat[0])):
            for i in range(len(_mat) - 1, 0, -1):
                _mat[i][j] = _mat[i-1][j]
                if (i == 1): _mat[0][j] = 'o'
    return _mat
def pomeriGore (mat, pomeraj):
    _mat = mat.copy()
    for k in range(pomeraj):
        for j in range(len(_mat[0])):
            for i in range(0, len(_mat) - 1):
                _mat[i][j] = _mat[i+1][j]
                if (i == len(_mat) - 2): _mat[len(_mat) - 1][j] = 'o'
    return _mat
def ispisiMatricu(mat):
    for i in range (len(mat)):
        for j in range (len(mat[0])):
            if (i == len(mat) - 1 and j == len(mat[0]) - 1): print (mat[i][j], end = "")
            elif (j == len(mat[0]) - 1): print (mat[i][j])
            else: print (mat[i][j], end = " ")

tabla = ucitavanjeMatrice()
linijaPomeraja = input().split()

desnoLevo = int(linijaPomeraja[0])
doleGore = int(linijaPomeraja[1])

if (desnoLevo > 0): tabla = pomeriDesno(tabla, desnoLevo)

else: pomeriLevo(tabla, -1 * desnoLevo)

if(doleGore > 0): pomeriDole(tabla, doleGore)
else: pomeriGore(tabla, -1 * doleGore)

ispisiMatricu(tabla)