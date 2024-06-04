import numpy as np

# ========================================================
# Función Esfera
# Dimensiones: d, xi = [-5.12, 5.12], para todo i = 1, .., d.
# Mínimo global 0 en (0, ..., 0)
# ========================================================
def esfera(X):
    return sum(x ** 2 for x in X)

# ========================================================
# Función Bohchevsky
# Dimensiones: 2, xi = [-100, 100], para todo i = 1, .., d.
# Mínimo global 0 en (0, ..., 0)
# ========================================================
def Bohchevsky(X):
    x1 = X[0]
    x2 = X[1]
    eq = (x1 ** 2) + 2 * (x2 ** 2) - 0.3 * np.cos((3 * np.pi * x1) + (4 * np.pi * x2)) + 0.3
    return eq

# ========================================================
# Función Booth
# Dimensiones: 2, xi = [-10, 10], para todo i = 1, .., d.
# Mínimo global 0 en (1, 3)
# ========================================================
def Booth(X):
    x1 = X[0]
    x2 = X[1]
    eq = ((x1 + 2 * x2 - 7) ** 2) + ((2 * x1 + x2 - 5) ** 2)
    return eq

# ========================================================
# Función Drop-Wave
# Dimensiones: 2, xi = [-5.12, 5.12], para todo i = 1, 2.
# Mínimo global -1 en (0, 0)
# ========================================================
def ola_caida(X):
    numerador = 1 + np.cos(12 * np.sqrt((X[0] ** 2) + (X[1] ** 2)))
    denominador = 0.5 * ((X[0] ** 2) + (X[1] ** 2)) + 2
    return -numerador / denominador

# ========================================================
# Función Eggholder
# Dimensiones: 2, xi = [-512, 512], para todo i = 1, 2.
# Mínimo global -959.6407 en (512, 404.2319)
# ========================================================
def eggholder(X):
    x1 = X[0]
    x2 = X[1]
    eq1 = -(x2 + 47) * np.sin(np.sqrt(abs(x2 + (x1 / 2) + 47)))
    eq2 = x1 * np.sin(np.sqrt(abs(x1 - (x2 + 47))))
    return eq1 - eq2

# ========================================================
# Función desconocida
# ========================================================
def desconocida(X):
    lista_abs = list(map(abs, X))
    suma_interna = np.sum(lista_abs)
    prod_interno = np.prod(lista_abs)
    return suma_interna + prod_interno
