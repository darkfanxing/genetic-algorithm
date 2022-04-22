from numpy import sum, abs, prod

def function_1(x):
    return sum(abs(x)) + prod(abs(x))