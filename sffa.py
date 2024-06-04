import numpy as np
import benchmark

POP_SIZE = 90
DIM_SIZE = 30
MAX_GEN = 100  # Incrementar el número de generaciones
ALPHA = 0.5  # Ajuste de alfa
BETA_MIN = 0.2  # Ajuste de beta mínimo
GAMMA = 1.0
BOUND = 100

LB = -BOUND * np.ones(DIM_SIZE)
UB = BOUND * np.ones(DIM_SIZE)

OBJ_FUNC = benchmark.esfera

# Generar luciérnagas
def generate_fireflies():
    return np.random.uniform(LB, UB, (POP_SIZE, DIM_SIZE))

def calculate_fitnesses(fireflies):
    return np.array([OBJ_FUNC(firefly) for firefly in fireflies])

def find_limits(fireflies):
    np.clip(fireflies, LB, UB, out=fireflies)

def update_alpha(alpha, gen):
    delta = 1 - (10 ** (-4) / 0.9) ** (1 / MAX_GEN)
    return (1 - delta) * alpha

fireflies = generate_fireflies()
best_fitnesses = []

for gen in range(MAX_GEN):
    ALPHA = update_alpha(ALPHA, gen)

    fitnesses = calculate_fitnesses(fireflies)
    sorted_indices = np.argsort(fitnesses)
    fireflies = fireflies[sorted_indices]
    fitnesses = fitnesses[sorted_indices]

    best_firefly = fireflies[0]
    best_fitness = fitnesses[0]
    best_fitnesses.append(best_fitness)

    scale = UB - LB
    for i in range(POP_SIZE):
        for j in range(POP_SIZE):
            if fitnesses[i] > fitnesses[j]:
                distance = np.linalg.norm(fireflies[i] - fireflies[j])
                beta = BETA_MIN + (1 - BETA_MIN) * np.exp(-GAMMA * (distance ** 2))
                random_step = ALPHA * (np.random.rand(DIM_SIZE) - 0.5) * scale
                fireflies[i] += beta * (fireflies[j] - fireflies[i]) + random_step

    find_limits(fireflies)

    print(f'Generación: {gen} - Mejor: {best_fitness}')

print(f'Generación: {MAX_GEN - 1} - Mejor: {best_fitness}')
print('fin de la ejecución')
