from numpy import cos, sum, power

def function_3(x):
    second_term = 1
    for index in range(len(x)):
        second_term *= cos(x[index] / (index + 1))
    return (1/4000) * sum(power(x, 2)) - second_term + 1