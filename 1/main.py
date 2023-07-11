# Project Euler Question 1
# The goal is to find the sum of all numbers between 1 and 1000 that are divisible by 3 or 5

# Create a function to determine if a number is divisible by 3 or 5
def is_divisible_by_3_or_5(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    else:
        return False
    
# For all numbers between 1 and 1000, determine if they are divisible by 3 or 5
# If they are, add them to a sum

sum = 0
for i in range(1, 1000):
    if is_divisible_by_3_or_5(i):
        sum += i

print(sum)
    