import math
import numpy as np
import matplotlib.pyplot as plt

oper = '0'
foo = '3'
teta = ((math.sqrt(5) - 1) / 2)
target = 0.1
results = {
    'goldenRes': []
}

def printRes (arr, method, fCalc, a, b, lamb):
    obj = arr[len(arr) - 1]
    match method:
        case 'gold':
            b1, a1 = b, a
            txt = 'GOLDEN_RATIO_RESULT'
            i2target = (np.log((b1 - a1) / target) / np.log(teta))# could use //
            print(f"{txt:_^93}")

    if a > b:
        n = a
        a = b
        b = n

    print(f'a = {a1} | b = {b1} | l = {target} | eps = {eps}')
    print(f'x in bounds of{a: >23.4f}:{b:.4f}\nResult is: {(a + b) / 2: >26.4f}')
    print(f'Iterations calculated: {len(arr): >9}\nFoo Calculated: {fCalc: >16}')# \nIterations for target: {: >9}'.format(len(arr), math.floor(i2target)))
    print('Length by calculated values: {: >7.3f} \nLength by formula: {: >17.3f}'.format(b-a, target/(b1-a1)))
    print(f'Function result: {lamb:^32.3f}')
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

def getFooRes (x, num, y, v, y1):
    match num:
        case '1':
            x = (4 * ((x**2 - 2*x - 8) * (x**2 - 9)) / (x**2 - x**4 + 0.000001))
        case '2':
            x = (x**3 + 2*(x**2) - x + 2)
        case '3':
            if oper == '0':
                x2 = y1[1]
                # x1 = y
                x = ((((y + (x * v)))**2) - ((-x2)**2) + ((y + (x * v)) * x2) - (y + (x * v)) + (x2 * 2))
            elif oper == '1':
                x1 = y1[0]
                # x2 = y
                x = (((-x1)**2) - (((y + (x * v)))**2) + (x1 * (y + (x * v))) - x1 + ((y + (x * v)) * 2))
            # x = (y + (x * v))
    return x

class iter_info:
    def __init__(self, k):
        self.k = k + 1
    def getInfo(self):
        print(f'|{self.k:^4}|{self.a: >13.4f}|{self.b: >13.4f}|{self.Lambda: >14.4f}|{self.Mu: >12.4f}|{self.FLamb: >15.4f}|{self.FMu: >14.4f}|')
    def calc(self, method, y, v, y1, goldFlag):
        match method:
            case 'gold':
                match goldFlag:
                    case 0:
                        self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
                        self.Mu = (self.a + teta * (self.b - self.a))
                        print('count both')
                    case 1:
                        self.Mu = (self.a + teta * (self.b - self.a))
                        print('count MU')
                    case 2:
                        self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
                        print('count lamb')
            
        self.FLamb = getFooRes(self.Lambda, foo, y, v, y1)
        self.FMu = getFooRes(self.Mu, foo, y, v, y1)
        
        
        # self.FLamb = getFooRes(self.Lambda, foo)
        # self.FMu = getFooRes(self.Mu, foo)

def getGoldenRatioRes (a, b, y, vect, y1):
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
        arr.calc(method, y, vect, y1, goldFlag)
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
            arr1.calc(method, y, vect, y1, goldFlag)
        else:
            goldFlag = 2
            fCalc += 1
            arr1.a, arr1.b = arr.a, arr.Mu
            arr1.Mu = arr.Lambda
            arr1.calc(method, y, vect, y1, goldFlag)
        goldFlag = 0
        k += 1
        arr = res[k]
        a, b = arr.a, arr.b
    arr.calc(method, y, vect, y1, goldFlag)
    printRes(res, method, fCalc, a, b, arr.FLamb)
    return arr.FLamb

eps = 0.01
vectors = {
    '0': [1.0, 0.0],
    '1': [0.0, 1.0]
}
x1 = [0.0, 0.0]
y1 = x1
k = j = 1
val = {
    'dots': []
}
dots = val['dots']
# dots.append(y1)
# print(val)
# dots.append([0.0, 0.0])
# ang = 100
# for j in range(len(vectors)):
#     vector = vectors[f'{j}']
#     oper = f'{j}'
#     lamb = getGoldenRatioRes(y1[j] - 5, y1[j] + 5, y1[j], vector[j], y1)
#     y2 = (y1[j] + (lamb * vector[0]))
#     print(f'{lamb}')
#     y1[j] = lamb
#     dots[k][j] = lamb
#     print(y1)
#     print(dots)
#     if j == 1:
#         # dot = y1
#         # dots.append(dot)
#         dots[0] = [0.0, 0.0]
#         print(dots)
#         ang = dots[-1][0] - dots[-2][0] + dots[-1][1] - dots[-2][1]
ang = 10
print(ang, eps)
while (ang > eps):
    dots.append(y1)
    print(val)
    dots.append([0.0, 0.0])
    for j in range(len(vectors)):
        vector = vectors[f'{j}']
        oper = f'{j}'
        lamb = getGoldenRatioRes(dots[k-1][j] - 5, dots[k-1][j] + 5, dots[k-1][j], vector[j], dots[k-1])
        y2 = (y1[j] + (lamb * vector[0]))
        print(f'{lamb}')
        y1[j] = lamb
        dots[k][j] = lamb
        print(dots)
        if j == 1:
            dot = y1
            dots.append(dot)
            dots[0] = [0.0, 0.0]
            print(dots)
            ang = dots[-1][0] - dots[-2][0] + dots[-1][1] - dots[-2][1]
            print(ang)
            k += 1

print(val)
# f = (((-x1)**2) - ((-x2)**2) + (x1 * x2) - x1 + (x2 * 2))

