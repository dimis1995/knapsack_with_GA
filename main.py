import operator
import random

mutation_rate = 0.1  # 0.2 # 0.5
population_size = 10  # 100 # 10000


def genetic_algorithm(weights: list, values: list, limit: int, optimal_solution: list):
    iteration = 0
    starting_pop = get_random_initial_population(len(weights))
    print("Generation 0: " + str(starting_pop))
    while optimal_solution not in starting_pop:
        new_generation = []
        best_solutions = evaluate_population(starting_pop, weights, values, limit)
        iteration += 1
        for i in range(0, len(best_solutions)):
            # print("Generation : " + str(iteration))
            r1 = best_solutions[i]
            r2 = None
            if i != len(best_solutions) - 1:
                r2 = best_solutions[i + 1]
            else:
                r2 = best_solutions[0]
            new_child1, new_child2 = crossover(r1, r2)
            new_generation.append(new_child1)
            new_generation.append(new_child2)
        for i in range(0, len(new_generation)):
            new_generation[i] = mutate(new_generation[i])
        starting_pop = new_generation
        print("Generation " + str(iteration) + " : " + str(starting_pop))
    print("solution found after " + str(iteration) + " generations")
    return iteration


def get_random_initial_population(solution_length: int):
    population = []
    for i in range(0, population_size):
        solution = []
        for j in range(0, solution_length):
            solution.append(random.randint(0, 1))
        population.append(solution)
    return population


def evaluate_population(pop: list, weights: list, values: list, limit: int):
    fitness_solution_list: [int, list] = []
    best_solutions = []
    for i in range(len(pop)):
        fitness_solution_list.append([fitness(pop[i], weights, values, limit), pop[i]])
    fitness_solution_list.sort(key=operator.itemgetter(0), reverse=True)
    for i in range(len(pop) // 2):
        best_solutions.append(fitness_solution_list[i][1])
    return best_solutions


def fitness(child: list, weights: list, values: list, limit: int):
    value = 0
    weight = 0
    for i in range(0, len(child)):
        if child[i] == 1:
            value += values[i]
            weight += weights[i]
    if weight <= limit:
        return value
    else:
        return -1


def mutate(child: list):
    result = []
    for i in range(0, len(child)):
        if random.uniform(0, 1) < mutation_rate:
            if child[i] == 0:
                result.append(1)
            else:
                result.append(0)
        else:
            result.append(child[i])
    return result


def crossover(child1: list, child2: list):
    threshold = random.randint(1, len(child1) - 1)
    tmp1 = child1[threshold:]
    tmp2 = child2[threshold:]
    ch1 = child1[:threshold]
    ch2 = child2[:threshold]
    ch1.extend(tmp2)
    ch2.extend(tmp1)
    return ch1, ch2


if __name__ == '__main__':

    limit1 = 165
    weights1 = [23,
                31,
                29,
                44,
                53,
                38,
                63,
                85,
                89,
                82]
    values1 = [92,
               57,
               49,
               68,
               60,
               43,
               67,
               84,
               87,
               72]
    optimal1 = [1,
                1,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                0]

    limit2 = 26
    weights2 = [12,
                7,
                11,
                8,
                9]
    values2 = [24,
               13,
               23,
               15,
               16]
    optimal2 = [0,
                1,
                1,
                1,
                0]

    limit3 = 190
    weights3 = [56,
                59,
                80,
                64,
                75,
                17]
    values3 = [50,
               50,
               64,
               46,
               50,
               5]
    optimal3 = [1,
                1,
                0,
                0,
                1,
                0]

    iterations = []
    for i in range(0, 10):
        iterations.append(genetic_algorithm(weights1, values1, limit1, optimal1))
        iterations.append(genetic_algorithm(weights2, values2, limit2, optimal2))
    print(iterations)
    iteration_sum = 0
    for i in iterations:
        iteration_sum += i
    print(iteration_sum // len(iterations))
