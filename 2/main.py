# Project Euler Question 2
# The goal is to find the sum of all even numbers in the Fibonacci sequence that are less than 4,000,000

# Create a function to determine if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Create a function to generate the Fibonacci sequence
def generate_fibonacci_sequence(maximum):
    fibonacci_sequence = [1, 2]
    while fibonacci_sequence[-1] < maximum:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
                                  
    return fibonacci_sequence

# For all numbers in the Fibonacci sequence, determine if they are even
# If they are, add them to a sum

sum = 0
for i in generate_fibonacci_sequence(4000000):
    if is_even(i):
        sum += i

print(sum)