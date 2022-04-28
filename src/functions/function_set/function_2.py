from numpy import power, sum

def function_2(x, dimension=30):
    result = 0
    for index in range(dimension):
        result += power(sum(x[:index]), 2)
    
    return result