import random

"""
Will find the number of generations to 'evolve' to input string

Shorter input string = less generations to find input string
Larger population size -> less generations to find input string
Mutation rate between 0.04 - 0.08 optimal
    -> Mutation rate 1 means brute force algorithm
    -> Not enough mutation leads to identical generations
"""
def main(input_string, mutation_rate, pop_size):
    input_len = len(input_string)
    curr_gen_strings = initialize(input_len, pop_size)
    fitness_array = [0 for i in range(len(curr_gen_strings))]
    found = False
    num_generations = 0
    while found == False:
        print(curr_gen_strings)
        fitness_array = check_fitness(curr_gen_strings, input_string)
        max_element_index = 0
        for i in range(1,len(fitness_array)):
            if fitness_array[i] > fitness_array[max_element_index]:
                max_element_index = i
        if (fitness_array[max_element_index] == input_len):
            found = True
            print(num_generations)
        else:
            curr_gen_strings = create_next_generation(curr_gen_strings,
                             max_element_index, mutation_rate)
        num_generations += 1
        
def initialize(input_len, population_size):
    string_array = []
    for i in range(population_size):
        random_string = ''
        for j in range(input_len):
            random_string += chr(random.randint(65,122))
        string_array += [random_string]
    return string_array

def check_fitness(string_array, input_string):
    fitness_array = []
    for string in string_array:
        fitness_level = 0
        for i in range(len(string)):
            if (string[i] == input_string[i]):
                fitness_level += 1
        fitness_array += [fitness_level]
    return fitness_array

def create_next_generation(prev_gen_strings, max_element_index, mutation_rate):
    next_generation = []
    prev_gen_optim = prev_gen_strings[max_element_index]
    for i in range(len(prev_gen_strings)):
        new_string = ''
        for j in range(len(prev_gen_strings[0])):
            if random.random() < mutation_rate:
                new_string += chr(random.randint(65,122))
            else:
                new_string += prev_gen_optim[j]
        next_generation += [new_string]
    return next_generation
    
main("Hello_World", 0.09, 20)
