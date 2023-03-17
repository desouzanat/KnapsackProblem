# Nathalia De Souza -- MBFA and Genetic Algorithms -- 2/10/2023


import random as ran
import numpy as np
import GA

# knapsack items
Values = [23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10]
Weights =[7, 2, 6, 9, 1, 5, 6, 1, 3, 4, 7, 9, 3, 7, 3, 4, 5, 1, 5, 4]
maxWei = 45


# # generate a single candidtate solution
# initialCan = GA.Chromosome(20, Values, Weghts, maxWei)

# # determine fitness of a single candidate solution
# Fit = GA.fitnessCheck(Values, Weights, maxWei, initialCan)


# generate population of 20 candidate solutions
Pop = GA.Population(20, 20, Values, Weights, maxWei)

# select parents from population based on their fitness
# Parents = GA.Population.selection(Pop, 2)

# # generate children using crossover method between parents
# crossChildren = GA.crossover(Parents)

# # generate children using mutation method 
#    # Just like the crossover operation, the mutation does not always happen
# mutChildren = GA.mutation(crossChildren)

# decide if children will be born of crossover or reproduction
# Children = GA.reproduction(Parents)

# select parents
Parents = GA.NextGen(Pop, Values, Weights, maxWei)

# create new generation of children from parents
children = GA.NextGen.newGen(Parents)
# for i in range(len(NewGen)):
#     print("Child's Fitness:", NewGen[i].fitness)

# solve knapsack problem for population
solu = GA.solveKnapsack(Pop, 20,20, Values, Weights, maxWei)


