from cmath import pi, sin
import numpy as np


class function():
    def __init__(self, object_fuction):
        self.object_fuction = object_fuction
        self.dim = 0
        self.bounds = [0, 0]
        if object_fuction == 1:
            self.dim = 30
            self.bounds = [-10, 10]
        elif object_fuction == 2:
            self.dim = 30
            self.bounds = [-100, 100]
        elif object_fuction == 3:
            self.dim = 30
            self.bounds = [-600, 600]
        elif object_fuction == 4:
            self.dim = 30
            self.bounds = [-50, 50]
        elif object_fuction == 5:
            self.dim = 30
            self.bounds = [-50, 50]
        elif object_fuction == 6:
            self.dim = 2
            self.bounds = [-65, 65]
        elif object_fuction == 7:
            self.dim = 4
            self.bounds = [-5, 5]
        pass
    def fit(self, x) -> float: 
        if self.object_fuction == 1:
            return self.func_1(x)
        elif self.object_fuction == 2:
            return self.func_2(x)
        elif self.object_fuction == 3:
            return self.func_3(x)
        elif self.object_fuction == 4:
            return self.func_4(x)
        elif self.object_fuction == 5:
            return self.func_5(x)
        elif self.object_fuction == 6:
            return self.func_6(x)
        elif self.object_fuction == 7:
            return self.func_7(x)
    
    def func_1(self, x):
        return np.sum(np.abs(x))+np.prod(np.abs(x))
    def func_2(self, x):
        result = 0
        for i in range(self.dim):
            result += np.power(np.sum(x),2)
        return result
    def func_3(self, x):
        d = len(x)
        dd = 1
        for i in range(d):
            dd*= np.cos(x[i]/(i+1))
        return (1/4000)*np.sum(np.power(x,2))-dd+1
    def func_4(self, x):
        n = len(x)
        def u(x,a,k,m):
            if x>a:
                return k*np.power((x-a),m)
            elif x < -a:
                return k*np.power((-x-a),m) 
            else:
                return 0
        def y(x):
            return 1+(x+1)/4
        part1 = 10*np.power(np.sin(pi*y(x[0])),2)
        part2 = 0
        part3 = 0
        for i in range(n-1):
            part2+=np.power(y(x[i]-1),2)*(1+10*np.power(np.sin(pi*y(x[i+1])),2))+np.power((y(x[-1])),2)
        for j in range(n):
            part3+= u(x[j],10,100,4)
        return (pi/n)*(part1+part2)+part3
    def func_5(self, x):
        n = len(x)
        def u(x,a,k,m):
            if x>a:
                return k*np.power((x-a),m)
            elif x < -a:
                return k*np.power((-x-a),m) 
            else:
                return 0
        part1 = 0
        part2 = 0
        for i in range(n-1):
            part1+=np.power((x[i]-1),2)*(1+(np.power(np.sin(3*pi*x[i+1]),2)))
        for j in range(n):
            part2+= u(x[j],5,100,4)

        return 0.1*(np.power(np.sin(3*pi*x[0]),2) + part1 + np.power((x[-1]-1),2))*(1+np.power(np.sin(2*pi*x[-1]),2))+part2
    def func_6(self, x):
        ind = [-32, -16, 0, 16, 32]
        a=[]
        tmp =[]
        for i in range(25):
            tmp.append(ind[(i%5)])
        a.append(tmp)
        tmp =[]
        for i in range(5):
            for j in range(5):
                tmp.append(ind[(i%5)])
        a.append(tmp)
        part1 = 0
        for i in range(25):
            p2 = 0
            for j in range(2):
                p2 += np.power(x[j]-a[j][i],6)
            part1+= 1/((i+1)+p2)
        return 1/((1/500)+part1)
    def func_7(self, x):
        a = [0.1957, 0.1947, 0.1735, 0.1600, 0.0844, 0.0627, 0.0456, 0.0342, 0.0342, 0.0235, 0.0246]
        b = [0.25, 0.5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
        result = 0
        for i in range(11):
            result+= np.power((a[i]-((x[0]*(np.power(b[i],2)+b[i]*x[1]))/(np.power(b[i],2)+b[i]*x[2]+x[3]))),2)
        return result
