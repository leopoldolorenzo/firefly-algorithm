import numpy as np
import benchmark

TAM_POBLACION = 90
DIMENSION = 30
MAX_GEN = 50
ALPHA = 0.2
BETA_MIN = 1.0
GAMMA = 1.0
LIMITE = 100

LB = -LIMITE * np.ones(DIMENSION)
UB = LIMITE * np.ones(DIMENSION)

FUNCION_OBJETIVO = benchmark.esfera

# número total de evaluaciones de la función
num_eval = TAM_POBLACION * MAX_GEN

Mejor = []

# generar luciérnagas
def generar_luciernagas():
    return np.random.uniform(0, 1, (TAM_POBLACION, DIMENSION)) * (UB - LB) + LB

def calcular_aptitudes(luciernagas):
    return [FUNCION_OBJETIVO(i) for i in luciernagas]

def encontrar_limites(luciernagas):
    for i in range(TAM_POBLACION):
        np.where(luciernagas[i] > LIMITE, LIMITE, luciernagas[i])
        np.where(luciernagas[i] < -LIMITE, -LIMITE, luciernagas[i])

def actualizar_alpha(alpha):
    delta = 1 - (10 ** (-4) / 0.9) ** (1 / MAX_GEN)
    return (1 - delta) * alpha

luciérnagas = generar_luciernagas()

for gen in range(MAX_GEN):
    
    ALPHA = actualizar_alpha(ALPHA)

    aptitudes = calcular_aptitudes(luciérnagas)
    indice_ordenado = np.argsort(aptitudes)
    aptitudes.sort()

    luciérnagas = luciérnagas[indice_ordenado, :]

    luciérnagas_viejas = luciérnagas.copy()
    aptitudes_viejas = aptitudes.copy()

    mejor_luciérnaga = luciérnagas[0]
    mejor_aptitud = aptitudes[0]

    escala = abs(UB - LB)
    for i in range(TAM_POBLACION):
        for j in range(TAM_POBLACION):
            
            distancia = np.sqrt(np.sum((luciérnagas[i] - luciérnagas_viejas[j]) ** 2))
            if (aptitudes[i] > aptitudes_viejas[j]):
                beta0 = 1
                beta = (beta0 - BETA_MIN) * np.exp(-GAMMA * (distancia ** 2)) + BETA_MIN
                tmpf = ALPHA * (np.random.rand(DIMENSION) - 0.5) * escala
                
                luciérnagas[i] = luciérnagas[i] * (1 - beta) + luciérnagas[j] * beta + tmpf

    encontrar_limites(luciérnagas)

    Mejor.append(mejor_aptitud)
    print(f'Generación: {gen} - Mejor: {mejor_aptitud}')
print(f'Generación: {gen} - Mejor: {mejor_aptitud}')

print('fin de la ejecución')
