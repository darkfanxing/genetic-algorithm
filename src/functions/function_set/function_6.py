from numpy import power, empty

def function_6(x):
    def a():
        values = [-32, -16, 0, 16, 32]
        a_1 = values * 5
        a_2 = []
        for value in values:
            a_2 += [value] * 5
        
        return [a_1, a_2]
    
    term_1 = 0
    a = a()

    for j in range(25):
        part_term_2 = 0
        for i in range(2):
            part_term_2 += power(x[i] - a[i][j], 6)
        
        term_1 += 1 / ((j + 1) + part_term_2)

    return 1 / (1/500 + term_1)