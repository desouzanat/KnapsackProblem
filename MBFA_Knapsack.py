# Nathalia De Souza -- Assignment 2: MBFA and Genetic Algorithms -- 2/10/2023

import random as ran
from tabulate import tabulate

'''
Task 1

- Develop a Modified Brute-Force Algorithm (MBFA) in Python.
- Use you MBFA to solve the KNAPSACK problem with values and weights given below.
- Submit your code and a list of the three best solutions you found.
'''

'''
- MBFA_knapsack goes through N combinations of items and outputs two lists, weiTot and valTot, whose
final indices are a singular solution to the knapsack problem

- it iterates until the knapsack is filled with as many items as possible without exceeding the maxWei, 
OR until N trials are reached
'''

def MBFA_knapsack(nTrials, items, maxWei):
    global valTot, weiTot

    val = [] # value storage
    wei = [] # weight storage
    idx = [] # index number storage

    valTot = [] # storage for total value (each index is the sum of the previous indices)
    weiTot = [] # storage for total weight (each index is the sum of the previous indices)

    for i in range(nTrials): 
        # choose a random integer between 0 and 19
        x = ran.randint(0, 19)

        if x not in idx: # if the integer hasn't been chosen before...
            idx.append(x) # add the integer (which represents the chosen index number) to the list idx
            wei.append(items["Weights"][x]) # add the weight corresponding to that index
            val.append(items["Values"][x]) # add the value corresponding to that index

            weiTot.append(sum(wei)) # sum all of the weights and append weiTot with that number
            valTot.append(sum(val)) # sum all of the values and append valTot with that number

        if weiTot[-1] > maxWei: # if the sum of all the weights is greater than 45...
            # remove the last index from the following lists
            del weiTot[-1]
            del valTot[-1]
            del wei[-1]
            del val[-1] 
            del idx[-1]
            # re-run the for loop until it fills the knapsack without going over 45 kg or until nTrials are reached


'''
- bestVPPair iterates through the selected function N times and collects the (some number, 'repeats') 
best value/weight pairs
- it takes as inputes the:
    - number of intended iterations (nTrials)
    - the desired number of best solutions output (repeats)
    - the selected function (f)
    - an arbitrary number of arguments specifict to the selected function (*args)
        - in the case of MFBA_knapsack, it takes nTrials, a dict of items with values/weights, and 
        a max weight as inputs
'''
def bestVPPair(nTrials, repeats, f, *args):
    
    vals = []
    weis = []

    for i in range(nTrials): 
        f(*args) # run the selected function N times

        # collect the final valTot/weiTot values from the selected function in new lists
        vals.append(valTot[-1])
        weis.append(weiTot[-1])

        # write the final values to a tuple called pairs and sort its values in ascending order wrt the values
        pairs = tuple(zip(vals, weis))
        pairs = sorted(pairs)


    bestPairs = [] # storage for best pair values
    for i in range(0, repeats):
        # add the last and (since its sorted by value now) highest value from pairs to a new list called bestPairs
        bestPairs.append(pairs[-1])
        # remove the last/highest value from pairs
        pairs.remove(pairs[-1])
        # continue the loop for the entire range to get the top 3 results

    print ("\n\n**************")
    print("\nOut of", nTrials, "trials, the three best solutions are: \n")
    print(" Value", "     Weight")
    print(" $", bestPairs[0][0], "    ", bestPairs[0][1], "kg")
    print(" $", bestPairs[1][0], "    ", bestPairs[1][1], "kg")
    print(" $", bestPairs[2][0], "    ", bestPairs[2][1], "kg\n")
    print ("**************\n\n")


# knapsack items
items = {"Values": [23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10], 
         "Weights": [7, 2, 6, 9, 1, 5, 6, 1, 3, 4, 7, 9, 3, 7, 3, 4, 5, 1, 5, 4]}
maxWei = 45

bestVPPair(1000, 3, MBFA_knapsack, 1000, items, maxWei)
    
