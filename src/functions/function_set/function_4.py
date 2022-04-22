from cmath import pi
from numpy import power, sin

def function_4(x):
        def u(x, a, k, m):
            if x > a:
                return k * power((x - a), m)
            elif x < -a:
                return k * power((-x-a), m) 
            else:
                return 0
        def y(x):
            return 1 + (x + 1) / 4
        
        term_1 = 10 * power(sin(pi * y(x[0])), 2)
        term_2 = power((y(x[-1] - 1)), 2)
        term_3 = 0
        n = len(x)

        for index in range(n-1):
            term_2 += \
                power(y(x[index] - 1), 2) * (1 + 10 * power(sin(pi * y(x[index + 1])), 2))
        
        for index in range(n):
            term_3 += u(x[index], 10, 100, 4)
        
        return (pi/n) * (term_1 + term_2) + term_3