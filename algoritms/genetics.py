import random


def fitness(individual):
    # Fitness function - sum the values of the individual.
    return sum(individual)


def create_individual(length, min_val, max_val):
    # Create a random individual with specified length and value range.
    return [random.randint(min_val, max_val) for _ in range(length)]


def mutate(individual, min_val, max_val, mutation_rate=0.1):
    # Mutate an individual with a given mutation rate.
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.randint(min_val, max_val)
    return individual


def crossover(parent1, parent2):
    # Crossover two parents to create two children.
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


population_size = 20
length = 10
min_val, max_val = 0, 10
generations = 50

# Initialize the population.
population = [create_individual(length, min_val, max_val) for _ in range(population_size)]

for gen in range(generations):
    # Sort population based on fitness.
    population.sort(key=fitness, reverse=True)

    # Select the top individuals for crossover.
    top = population[:10]
    new_population = top.copy()

    # Create offspring by crossover.
    while len(new_population) < population_size:
        parents = random.sample(top, 2)
        children = crossover(parents[0], parents[1])
        new_population.extend(children)

    # Apply mutation to the new population.
    population = [mutate(ind, min_val, max_val) for ind in new_population]


