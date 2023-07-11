# Project Euler Problem 100
# The goal is to find the number of blue discs 
# for which the probability of taking two blue discs is exactly 1/2 
# when taken from a pile containing at least 10^12 discs.
import math

x, y = 1, 1
while x + 1 <= 2e12:
    x, y = 3*x + 4*y, 2*x + 3*y

print((y + 1) // 2)





