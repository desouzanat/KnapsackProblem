
# chromosome = candidate solution = individual
# genes = bits
# population = set of chromosomes/candidate solutions


import copy
import numpy as np
import random

class Chromosome:

    def __init__(self, numGenes):

        # create a random Boolean representation of whether an item is put into the knapsack
            # this is a random candidate solution (chromosome) made up of n bits (genes)
            # 1 = included, 0 = excluded
        self.genes = random.choices([0, 1], k = numGenes)


def fitnessCheck(values, weights, maxWei, chrom) -> int:

    # create a zipped list that relates each gene to an item's value and weight
    x = list(zip(chrom.genes, values, weights))
    v = []
    w = []

    for gene in range(0, len(chrom.genes)):
        
        # to find the total $ value and weight of a chromosome:
            # append the product of the gene (0 or 1) and the item's value/weight to an empty list
                # if a gene is included (1), the value/weight appended to the list is equal to the 
                # $ value/weight of the item
                # if a gene is not included (0), the value/weight appended to the list is 0
            # sum all of the values/weights in the lists to get the total value/weight of the chromosome

        # e.g., for x = [(1,2,3), (0,4,5), (1,6,7), (1,8,9)] 
            # v = [2, 0, 0, 8] & w = [3, 0, 0, 9]
            # totalValue = 10 & totalWeight = 12

        v.append(x[gene][0] * x[gene][1])
        totalValue = sum(v)

        w.append(x[gene][0] * x[gene][2])
        totalWeight = sum(w)
     
    if totalWeight <= maxWei: 
        # if totalWeight of the chromosome is <= the maximum allowable weight of the knapsack, 
        # the fitness coefficient of the chromosome is equal to its total value 
        chrom.fitness = totalValue
    # if totalWeight exceeds maxweight, the fitness coefficient is equal to 0
    else: chrom.fitness = 0
    
    return chrom.fitness
    

class Population:

    def __init__(self, populationSize, numGenes, values, weights, maxWei):

        # generate a population of members (chromosomes)
        self.members = [Chromosome(numGenes) for i in range(populationSize)]
        
        # calculate the fitness coefficient of each population member (chromosome)
        for i in range(populationSize):
            fitnessCheck(values, weights, maxWei, self.members[i])


    # select members to be "parents" of the next generation; 
    # ratio = number of population members we want in the tournament
    def selection(self, N) -> list:
    
        parents = []

        for i in range(N):
            # shuffle the population
            random.shuffle(self.members)
            
            # select the first 2 chromosomes to be the "parents" of the next generation
            if self.members[i].fitness > self.members[i + 1].fitness:
                parents.append(self.members[i])
            else: parents.append(self.members[i + 1])

        return parents
    

def mutation(children):

    kids = children
    for child in kids:
        # print(child)  # this is the child's chromosome before mutation
        for gene in range(len(kids)):
            flip = random.randint(0, 1) # randomly choose 1 or 0
            # if the number 1 is chosen, flip the bit at the index gene
            if flip == 1 and child.genes[gene] == 0:                     
                    child[gene] = 1
            elif flip == 1 and child[gene] == 1:
                child[gene] = 0
            # if the number 0 is chose, the gene stays the same
            else: child[gene] = child[gene]

            # print(child) # this is the child's chromosome after mutation
    # this returns both children after mutation
    return kids


class NextGen:
    def __init__(self, population, values, weights, maxWei) -> list:
        
        # select parents
        parents = Population.selection(population, 2)

        # make sure the parents have chromosomes and fitnesses
        self.members = []
        for i in range(len(parents)):
            self.members.append(parents[i]) # each member of self is a child
        

        # calculate the fitness coefficient of each child
        for i in range(len(self.members)):
            fitnessCheck(values, weights, maxWei, self.members[i])
        
        
    def crossover(self):

        parents = copy.deepcopy(self)
        children = []
        N = len(self[0].genes)

        # generate a random crossover point
        crossPoint = random.randint(0, N)

        # append the list children with two new chromosomes created by swapping the parent genes at the crossover point
            # this ONLY gives the genes, and NOT the associated fitnesses
        for i in range(len(self)):    
            self[i].genes.clear()
            self[i].fitness = 0
        self[0].genes = parents[0].genes[0:(crossPoint + 1)] + parents[1].genes[(crossPoint + 1):N]
        self[1].genes = parents[0].genes[(crossPoint + 1):N] + parents[1].genes[0:(crossPoint + 1)]
     
        children = self
        return children
        
    def newGen(self):
        children = []
        parents = copy.deepcopy(self)
        while len(children) < len(parents.members):

            reproOdd = random.random()
            crossOdd = random.random()
            mutOdd = random.random()
                
            # reproduction
            if reproOdd < 0.4:
                children = self
            else:
                # crossover
                if crossOdd < 0.6:
                    NextGen.crossover(parents)
                    children = self

                # mutation
                if mutOdd < 0.01:
                    mutation(self.members)
                    children = self

            # nextGen.extend(children)
        return children

def solveKnapsack(population, populationSize, numGenes, values, weights,maxWei):
    avgFit = []
    fits = []
    
    for i in range(populationSize):
        parents = NextGen(population, values, weights, maxWei)
        children = NextGen.newGen(parents)
        fit = children.members[i].fitness
        fits.append(fit)
    avgFit.append(np.mean(fits))
