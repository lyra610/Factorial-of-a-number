# A program to find the factorial of a number
import math

number = int(input('Enter the number to find factorial '))


def factorial_function(n):
    return math.factorial(n)


f = factorial_function(number)
print('The factorial of', number, 'is ', f)
