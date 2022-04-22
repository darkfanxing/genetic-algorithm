from cmath import pi
from numpy import power, sin

def function_5(x):
        def u(x, a, k, m):
            if x > a:
                return k * power((x-a), m)
            elif x < -a:
                return k * power((-x-a), m)
            else:
                return 0

        term_1 = power(sin(3 * pi * x[0]), 2) + power((x[-1] - 1), 2) * (1 + power(sin(2 * pi * x[-1]), 2))
        term_2 = 0
        n = len(x)
        
        for index in range(n-1):
            term_1 += power((x[index] - 1), 2) * (1 + power(sin(3 * pi * x[index+1]), 2))
        
        for index in range(n):
            term_2 += u(x[index], 5, 100, 4)

        return 0.1*(term_1) + term_2