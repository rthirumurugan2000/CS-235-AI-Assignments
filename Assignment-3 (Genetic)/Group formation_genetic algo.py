import random
random.seed(50)
from random import randint as rand
from statistics import variance, mean

def random_marks(size, start=40, end=80):
    return [rand(start, end) for i in range(size)]

def mutation(gene):
    mut_index = rand(0, len(gene) - 1)  #randomly changing value of a index
    gene[mut_index] = rand(1, 3)
    return gene

def fitness_function(encoded, marks):   # returns average of variance
    group_1, group_2, group_3 = list(), list(), list()
    for i in range(len(encoded)):
        if encoded[i] == 1:
            group_1.append(marks[i])
        elif encoded[i] == 2:
            group_2.append(marks[i])
        else:
            group_3.append(marks[i])

    var1 = variance(group_1) if len(group_1) > 1 else 0
    var2 = variance(group_2) if len(group_2) > 1 else 0
    var3 = variance(group_3) if len(group_3) > 1 else 0

    return mean([var1, var2, var3])

def make_population(num_s,ps):
    return [[rand(1, 3) for i in range(num_s)] for j in range(ps)]

def singlepoint_crossover(parent1, parent2):
    index = rand(1, len(parent1) - 1)
    offspring1 = parent1[:index] + parent2[index:]
    offspring2 = parent2[:index] + parent2[index:]
    return offspring1,offspring2
    

def genetic_algorithm(genes,marks):
    best_gene = genes[0]
    initial_fitness = fitness_function(best_gene, marks)
    final_fitness = initial_fitness
    #len(genes)
    for i in range(len(genes)):
        for j in range(i + 1, len(genes)):
            gene1, gene2 = singlepoint_crossover(genes[i], genes[j])
            prob = rand(0, 1)  #checking whether to mutate based on prob
            if prob:
                gene1 = mutation(gene1)
                gene2 = mutation(gene2)
            if fitness_function(gene1, marks) < final_fitness:
                final_fitness = fitness_function(gene1, marks)
                best_gene = gene1
            if fitness_function(gene2, marks) < final_fitness:
                final_fitness = fitness_function(gene2, marks)
                best_gene = gene2

    return best_gene, final_fitness, initial_fitness


    

def main():
    num_students = int(input("Enter number of Students\n"))
    #num_students = 10
    population_size = int(input("Choose population size\n"))  #initial subset of solutions
    #population_size = 100
    #marks = [12,13,14,45,46,52,71,82,85,87]
    marks = random_marks(num_students)
    genes = make_population(num_students,population_size)# generates population
    best_gene, final_fitness, initial_fitness = genetic_algorithm(genes, marks)
    print("MARKS = {}\n".format(marks))
    print("INITIAL FITNESS = {}\n".format(initial_fitness))
    print("INITIAL GENE = {}\n".format(genes[0]))
    print("FINAL FITNESS = {}\n".format(final_fitness))
    print("best gene = {}".format(best_gene))
       
    
    
if __name__ == '__main__':
    main()
