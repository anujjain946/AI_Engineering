'''
 This file operates as a module which contains all the required 
 functions of calculator
'''
def square(num):
    '''This function returns the square of that number'''
    return num ** 2

def cube(num):
    '''This function returns the cube of that number'''
    return num ** 3

def factorial(num):
    '''This function returns the factorial of a given number'''
    # base case condition
    if num == 0 or num == 1:
        return 1
    else:
        # recursion
        return num * factorial(num - 1)

def add(num1, num2):
    '''This function returns the addition of two numbers'''
    return num1+num2

def subtract(num1, num2):
    '''This function returns the subtraction of two numbers'''
    return num1 - num2

def multiply(num1, num2):
    '''This function returns the multiplication of two numbers'''
    return num1 * num2

def divide(num1, num2):
    try:
        result = num1/num2
    except:
        print("An error occurred")
    else:
        return result
    