from typing import Callable, Tuple, List
from random import random
from numpy.random import randint

def decode_chromosome(boundaries, number_bit, bit_strings):
    decoded_bit_strings = []
    largest_number = 2**number_bit
    for index in range(len(boundaries)):
        substring = bit_strings[index * number_bit:(index + 1) * number_bit]
        binary_number = int("".join([str(string) for string in substring]), base=2)
        value = boundaries[index][0] + (binary_number/largest_number) * (boundaries[index][1] - boundaries[index][0])
        decoded_bit_strings.append(value)
    
    return decoded_bit_strings

def select(population, scores, k=3):
    selection_index = randint(len(population))
    for index in randint(0, len(population), k-1):
        if scores[index] < scores[selection_index]:
            selection_index = index

    return population[selection_index]

# crossover two parents to create two children
def crossover(parent_1, parent_2, cross_rate):
    if random() < cross_rate:
        cut_index = randint(1, len(parent_1) - 2)
        children_1 = parent_1[:cut_index] + parent_2[cut_index:]
        children_2 = parent_2[:cut_index] + parent_1[cut_index:]
    else:
        children_1, children_2 = parent_1, parent_2

    return [children_1, children_2]

# mutation operator
def mutation(bit_strings, mutation_rate):
    for index in range(len(bit_strings)):
        if random() < mutation_rate:
            bit_strings[index] = 1 - bit_strings[index]

    return bit_strings

def genetic_algorithm(
    function_: Callable,
    boundaries: List[List[float]],
    number_bit: int,
    number_iteration: int,
    number_population: int,
    cross_rate: float,
    mutation_rate: float
) -> Tuple[List[int], float, List[float]]:
    populations = [list(randint(0, 2, number_bit * len(boundaries))) for _ in range(number_population)]
    best_fitness_set = []
    best_fitness = function_(decode_chromosome(boundaries, number_bit, populations[0]))
    best_solution = None
    
    for _ in range(number_iteration):
        decoded_chromosomes = [decode_chromosome(boundaries, number_bit, population) for population in populations]
        fitnesses = [function_(decoded_bit) for decoded_bit in decoded_chromosomes]
        
        for index in range(number_population):
            if fitnesses[index] < best_fitness:
                best_solution = populations[index]
                best_fitness = fitnesses[index]

        best_fitness_set.append(best_fitness)
        parent_chromosomes = [select(populations, fitnesses) for _ in range(number_population)]

        children = []
        for index in range(0, number_population, 2):
            parent_1, parent_2 = parent_chromosomes[index], parent_chromosomes[index+1]
            for child in crossover(parent_1, parent_2, cross_rate):
                children.append(mutation(child, mutation_rate))

        populations = children
    
    return decode_chromosome(boundaries, number_bit, best_solution), best_fitness, best_fitness_set
