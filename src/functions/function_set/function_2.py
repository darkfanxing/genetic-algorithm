from numpy import power, sum

def function_2(x, dimension=30):
    result = 0
    for _ in range(dimension):
        result += power(sum(x), 2)
    
    return result