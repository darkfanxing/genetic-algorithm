from numpy import power

def function_7(x):
    a = [0.1957, 0.1947, 0.1735, 0.1600, 0.0844, 0.0627, 0.0456, 0.0342, 0.0342, 0.0235, 0.0246]
    b = [0.25, 0.5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
    answer = 0
    for index in range(len(a)):
        answer += \
            power(
                a[index] \
                    - (
                        (x[0] * (power(b[index], 2) + b[index] * x[1]))
                        / (power(b[index], 2) + b[index] * x[2] + x[3])
                    ),
                2
            )
    
    return answer