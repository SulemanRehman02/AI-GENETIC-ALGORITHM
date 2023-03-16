import random

secret_word = "hello" #Add your test set
word_length = len(secret_word)
population_size = 50
generations = 100

# Create the initial population
population = []
for i in range(population_size):
    individual = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(word_length))
    population.append(individual)

# Define the fitness function
def fitness(individual):
    score = 0
    for i in range(word_length):
        if individual[i] == secret_word[i]:
            score += 1
    return score

# Define the selection function
def selection(population):
    fitnesses = [fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness/total_fitness for fitness in fitnesses]
    parents = random.choices(population, probabilities, k=2)
    return parents

# Define the crossover function
def crossover(parents):
    crossover_point = random.randint(1, word_length-1)
    child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
    child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
    return child1, child2

# Define the mutation function
def mutation(individual, probability):
    individual_list = list(individual)
    for i in range(word_length):
        if random.random() < probability:
            individual_list[i] = random.choice('abcdefghijklmnopqrstuvwxyz')
    return ''.join(individual_list)

# Run the genetic algorithm
for generation in range(generations):
    print(f"Generation {generation+1}")
    # Selection
    new_population = []
    for i in range(population_size//2):
        parents = selection(population)
        # Crossover
        child1, child2 = crossover(parents)
        # Mutation
        child1 = mutation(child1, 0.1)
        child2 = mutation(child2, 0.1)
        new_population.append(child1)
        new_population.append(child2)

    new_population[0] = max(population, key=fitness)
    population = new_population
    
    # Print the best individual
    best_individual = max(population, key=fitness)
    print(f"Best individual: {best_individual}")
    if best_individual == secret_word:
        print("Solution found!")
        break
