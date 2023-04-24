import math
import numpy as np
import matplotlib.pyplot as plt

oper = '0'
foo = '3'
teta = ((math.sqrt(5) - 1) / 2)
target = 0.1
eps = 0.1
results = {
    'goldenRes': []
}

def printRes (arr, method, fCalc, v, y1):
    arr = results['goldenRes']
    obj = arr[0]
    match method:
        case 'gold':
            b1, a1 = obj.b, obj.a
            txt = 'GOLDEN_RATIO_RESULT'
            i2target = (np.log((b1 - a1) / target) / np.log(teta))# could use //
            print(f"{txt:_^93}")

    if obj.a > obj.b:
        n = obj.a
        obj.a = obj.b
        obj.b = n

    print(f'a = {a1} | b = {b1} | l = {target} | eps = {eps}')
    print(f'x in bounds of{obj.a: >23.4f}:{obj.b:.4f}\nResult is: {(obj.a + obj.b) / 2: >26.4f}')
    print(f'Iterations calculated: {len(arr): >9}\nFoo Calculated: {fCalc: >16}')# \nIterations for target: {: >9}'.format(len(arr), math.floor(i2target)))
    print('Length by calculated values: {: >7.3f} \nLength by formula: {: >17.3f}'.format(obj.b-obj.a, target/(b1-a1)))
    print(f'Function result: {getFooRes((obj.a + obj.b) / 2, foo, v, y1):^32.3f}')
    print(f'{"":-^93}')
    print("| k  |      a      |      b      |    lambda    |     mu     |   F(lambda)   |     F(mu)    |")
    print(f'{"":-^93}')
    for i in range(len(arr)):
        arr[i].getInfo()
    # z = ((obj.a + obj.b) / 2)
    # x = np.arange(obj.a, obj.b, eps)
    # plt.axvline(x = obj.a, color = 'black')
    # plt.axvline(x = obj.b, color = 'black')
    # plt.axvline(x = z, color = 'red')
    # y = obj.FLamb
    # plt.plot(x, y, color='blue')
    # plt.show()

def getFooRes (x, num, v, y1):
    match num:
        case '1':
            x = (4 * ((x**2 - 2*x - 8) * (x**2 - 9)) / (x**2 - x**4 + 0.000001))
        case '2':
            x = (x**3 + 2*(x**2) - x + 2)
        case '3':
            if oper == '0':
                x2 = y1[1]
                y = y1[0]
                # x1 = y
                x = ((((y + (x * v)))**2) - ((-x2)**2) + ((y + (x * v)) * x2) - (y + (x * v)) + (x2 * 2))
            elif oper == '1':
                x1 = y1[0]
                y = y1[1]
                # x2 = y
                x = (((-x1)**2) - (((y + (x * v)))**2) + (x1 * (y + (x * v))) - x1 + ((y + (x * v)) * 2))
            # x = (y + (x * v))
    return x

class iter_info:
    def __init__(self, k):
        self.k = k + 1
    def getInfo(self):
        print(f'|{self.k:^4}|{self.a: >13.4f}|{self.b: >13.4f}|{self.Lambda: >14.4f}|{self.Mu: >12.4f}|{self.FLamb: >15.4f}|{self.FMu: >14.4f}|')
    def calc(self, method, v, y1, goldFlag):
        match method:
            case 'gold':
                match goldFlag:
                    case 0:
                        self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
                        self.Mu = (self.a + teta * (self.b - self.a))
                        # print('count both')
                    case 1:
                        self.Mu = (self.a + teta * (self.b - self.a))
                        # print('count MU')
                    case 2:
                        self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
                        # print('count lamb')
            
        self.FLamb = getFooRes(self.Lambda, foo, v, y1)
        self.FMu = getFooRes(self.Mu, foo, v, y1)
        
        
        # self.FLamb = getFooRes(self.Lambda, foo)
        # self.FMu = getFooRes(self.Mu, foo)

def getGoldenRatioRes (a, b, vect, y1):
    k, fCalc = 0, 0
    goldFlag = 0
    method = 'gold'
    res = results['goldenRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b = a, b
    fCalc += 2
    while b - a > target:
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        arr.calc(method, vect, y1, goldFlag)
        fCalc += 0
        match foo:
            case '1':
                foper = arr.FLamb
                soper = arr.FMu
            case '2':
                foper = arr.FMu
                soper = arr.FLamb
            case '3':
                foper = arr.FLamb
                soper = arr.FMu
        if foper > soper:
            goldFlag = 1
            fCalc += 1
            arr1.a, arr1.b = arr.Lambda, arr.b
            arr1.Lambda = arr.Mu
            arr1.calc(method, vect, y1, goldFlag)
        else:
            goldFlag = 2
            fCalc += 1
            arr1.a, arr1.b = arr.a, arr.Mu
            arr1.Mu = arr.Lambda
            arr1.calc(method, vect, y1, goldFlag)
        goldFlag = 0
        k += 1
        arr = res[k]
        a, b = arr.a, arr.b
    arr.calc(method, vect, y1, goldFlag)
    # printRes(res, method, fCalc, vect, y1)
    results['goldenRes'] = []
    return [arr.Lambda, arr.FLamb]

x1 = 0.0
x2 = 0.0
x = [x1, x2]
xs = x
vectors = {
    '0': [0.0, 1.0],
    '1': [1.0, 0.0]
}
y = x
k = 0
j = 0

def printRess(k, x, fx, j, d, y, lamb, y1):
    print(f'|  k  |  xk  |  j  |  dj  |  yj  |  labmj  |  yj+1  |')
    print(f'|  {k}|  {x} | {j} |  {d} |  {y} | {lamb}  | {y1}   |')

ang = 10
while ang > eps:
    k += 1
    j += 1
    lamb = getGoldenRatioRes(x[0] - 10, x[0] + 10, 1.0, y)
    y[0] += lamb[0]
    fl = lamb[1]
    x = y
    d = vectors[f'{j - 1}']
    # printRess(k, [x1, x2], fl, j, d, y, lamb, x)
    print(f'x = {lamb[0], lamb[1]}')

    j += 1
    lamb = getGoldenRatioRes(x[1] - 10, x[1] + 10, 1.0, y)
    y[1] += lamb[0]
    fl = lamb[1]
    ang = abs(x1 - y[0]) + abs(x2 - y[1])
    x = y
    d = vectors[f'{j - 1}']
    print(f'y = {lamb[0], lamb[1]}')

    print(ang)
    x1, x2 = y[0], y[1]
    j = 0

# lamb = getGoldenRatioRes(x[0] - 2, x[0] + 2, 1.0, y)
# y[0] += lamb
# x = y
# lamb = getGoldenRatioRes(x[0] - 2, x[0] + 2, 1.0, y)
# y[1] += lamb
# ang = abs(x1 - y[0]) + abs(x2 - y[1])
# x = y
# print(ang)

