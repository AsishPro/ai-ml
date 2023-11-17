import numpy as np

#everything is generated randomly
#algorithm:
#1.generate distance(randomly)
#2.generate population (sequence of cities) (initial)
#3.at each iteration shuffle population, find fitness for current population 
#  and assign propabilites based on fitness
#4.select new population from current (for parents) based on assigned probability
#  directly can be done using np.choice
#5.using two parents from population find two children, with crossover and mutation(randomly)
# add these children to empty list 
#6. keep doing for all parents
#7. this children is new population, next generation


# initial population
def ini_population(population_size, n):
    return np.array([np.random.permutation(n) for i in range(population_size)])
# print(population(population_size,n))

# distance of a path
def calculate_distance(path, distances):
    distance = 0
    for i in range(len(path) - 1):
        distance += distances[path[i]][path[i + 1]]
    distance += distances[path[-1]][path[0]]  # Return to the starting city
    return distance
# print(calculate_total_distance([0,1,2,3,4,5,6,7,8,9],distances))

def crossover(p1, p2):
    child = [-1] * len(p1)
    # print(child)
    start, end = sorted(np.random.randint(0, len(p1), 2))
    child[start:end] = p1[start:end]
    remaining = [item for item in p2 if item not in child]
    remaining_index = 0
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = remaining[remaining_index]
            remaining_index += 1
    return np.array(child)


def mutate(path):
    id1, id2 = np.random.randint(0, len(path), 2)
    path[id1], path[id2] = path[id2], path[id1]
    return path

#finds fitness based for group
def find_fitness(population,distances):
    return np.array([1 / calculate_distance(path, distances) for path in population])

#genetic algo
def GA(distances, population_size, mutation_rate, generations):
    population = ini_population(population_size, n) #make population
    for generation in range(generations):
        fitness = find_fitness(population,distances)
        parents = population[np.random.choice(population_size, size=population_size, p=fitness/fitness.sum())]
        children = []
        for i in range(0,population_size,2):
            p1, p2 = parents[i], parents[i + 1]
            child1 = crossover(p1, p2)
            child2 = crossover(p2, p1)  # Swap parents for the second child
            if np.random.rand() < mutation_rate:
                child1 = mutate(child1)
            if np.random.rand() < mutation_rate:
                child2 = mutate(child2)
            children.append(child1)
            children.append(child2)
        population = np.array(children[:population_size])  # Keep only the top population_size children
    best_index = np.argmax(find_fitness(population,distances))
    # print(best_index)
    best_path = population[best_index]
    return best_path, calculate_distance(best_path,distances)

#ex: 10 cities
n= 10

distances = np.random.randint(1, 100, size=(n,n))
print("Distances: ")
print(distances)

population_size = 100
#to mutate randomly
mutation_rate = 0.01 
num_generations = 100

best_path, best_distance = GA(distances, population_size, mutation_rate, num_generations)
print("Best path:", best_path)
print("Best Distance:", best_distance)
