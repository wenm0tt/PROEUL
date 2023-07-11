# Project Euler Problem 851

# Here is an example. 
# For the Sum of all the products in a set that is 1 element long being 10, 
# what is the product of the sums?

# you can have the set be (1) and (10) or (2) and (5) or (10) and (1) or (5) and (2)

# we have 2 pieces of information: the tuple length and the SOP
# take the SOP and split it into all possible addend groups with n addends
# then take each addend in each group and split it into a potential product of 2 integers
# now we have all the 'u' and 'v' groups so all we must do is take u1 and v1, add them together,
# and then multiply them by u2 and v2, and so on until we have the final product
# this product will be the product for this set of us and vs
# for all u and v groups, find the product, then add them together
# then do that for another set of addends

# Currently my code does not work for high values of n and SOP because the 
# amount of time it takes for the distribute sums function is too high

import math
from tqdm import tqdm

def distribute_sum(sum_value, n):
    if sum_value <= 0 or n <= 0:
        return []
    
    addends = []
    distribute_sum_helper(sum_value, n, [], addends)
    return addends

def distribute_sum_helper(remaining_sum, remaining_addends, current_distribution, addends):
    if remaining_addends == 0:
        if remaining_sum == 0:
            addends.append(current_distribution[:])
        return
    
    for i in range(remaining_sum + 1):
        current_distribution.append(i)
        distribute_sum_helper(remaining_sum - i, remaining_addends - 1, current_distribution, addends)
        current_distribution.pop()

def factor_pairs(number):
    if number <= 0:
        return []
    
    pairs = []
    for i in range(1, number + 1):
        if number % i == 0:
            pairs.append([i, number // i])
    return pairs

def R(n, SOP):
    ALL_Us = []
    ALL_Vs = []
    cores = distribute_sum(SOP, n)
    bigSUMMA = 0
    for core in cores:
        THIS_Us = []
        THIS_Vs = []
        SUMMA = 1
        for num in core:
            potential_uvs = factor_pairs(num)
            miniSUM = 0
            for pair in potential_uvs:
                miniSUM += pair[0] + pair[1]
            SUMMA *= miniSUM
        bigSUMMA += SUMMA
    return bigSUMMA

print(R(3, 1000))
    
