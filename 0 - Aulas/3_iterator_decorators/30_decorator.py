"""
DECORATOR
 - Closures & Syntax Sugar
 - Apply : Timing; Debug; Register; Track state; Cache; Closure; Log factory
 - Decorator with arguments

"""
import functools

def calculate_food():
    print("INSIDE: A0")

    def discount():
        print("INSIDE: B0")

    print("INSIDE: A1")
    discount()
    print("INSIDE: A2")

calculate_food()
#

def calculate_gas(x):
    def discount(y):
        return y * 0.9
    
    price = discount(x)
    return f"Final price is: {price} \n"

print( calculate_gas(10) )

# Function parameters
def g():
    print("FUNCTION G")

def f(func):
    print("FUNCTION F")
    func()
    print("func's real name is " + func.__name__ , '\n') 

f(g)

#
def f1(x):
    def g1(y):
        return y + x + 1

    return g1(x)

print( f1(2) )

#
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")
