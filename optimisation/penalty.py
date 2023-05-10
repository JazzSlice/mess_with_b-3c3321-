import math
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

oper = '0'
foo = '2'
teta = ((math.sqrt(5) - 1) / 2)
target = 0.1
results = {
    'goldenRes': []
}

def printRes (arr, method, fCalc, v, y1):
    arr = results['goldenRes']
    obj = arr[-1]
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
    print(f'Function result: {obj.FLamb:^32.3f}')
    print(f'{"":-^93}')
    print("| k  |      a      |      b      |    lambda    |     mu     |   F(lambda)   |     F(mu)    |")
    print(f'{"":-^93}')
    for i in range(len(arr)):
        arr[i].getInfo()


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
                    case 1:
                        self.Mu = (self.a + teta * (self.b - self.a))
                    case 2:
                        self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
        match foo:
            case '2':
                self.FLamb = getFoo(self.Lambda, v, y1, 'e')
                self.FMu = getFoo(self.Mu, v, y1, 'e')
            case '1':
                self.FLamb = getFoo(self.Lambda, v, y1, 'p')
                self.FMu = getFoo(self.Mu, v, y1, 'p')

def getGoldenRatioRes (vect, y1, rng):
    k, fCalc = 0, 0
    goldFlag = 0
    method = 'gold'
    res = results['goldenRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b = -rng, rng
    fCalc += 2
    arr.calc(method, vect, y1, goldFlag)
    while arr.b - arr.a > eps:
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        arr.calc(method, vect, y1, goldFlag)
        fCalc += 0
        match foo:
            case '1':
                foper = arr.FMu
                soper = arr.FLamb
            case '2':
                foper = arr.FLamb
                soper = arr.FMu
        if foper > soper:
            goldFlag = 1
            fCalc += 1
            arr1.a, arr1.b = arr.Lambda, arr.b
            arr1.Lambda = arr.Mu
            arr1.Mu = (arr1.a + teta * (arr1.b - arr1.a))
            arr1.calc(method, vect, y1, goldFlag)
        else:
            goldFlag = 2
            fCalc += 1
            arr1.a, arr1.b = arr.a, arr.Mu
            arr1.Mu = arr.Lambda
            arr1.Lambda = (arr1.a + (1 - teta) * (arr1.b - arr1.a))
            arr1.calc(method, vect, y1, goldFlag)
        goldFlag = 0
        k += 1
        arr = res[k]
    
    return [round((abs(arr.a - arr.b)) / 2, roun), arr.Lambda]

def getFoo(lamb=0, d=[0,0], x=[0,0], goal='f'):
    lamb = lamb
    func = foon
    match goal:
        case 'f':
            func = foon
            func = func.replace('x1', str(x[0]))
            func = func.replace('x2', str(x[1]))
            func = func.replace('a(x)', str(0))
            res = round(eval(func), roun)
        case 'e':
            func1 = str(foon)
            x1 = '(x[0] + (lamb * d[0]))'
            x2 = '(x[1] + (lamb * d[1]))'
            func1 = func1.replace('x1', x1)
            func1 = func1.replace('x2', x2)
            func1 = func1.replace('x[0]', str(x[0]))
            func1 = func1.replace('x[1]', str(x[1]))
            func1 = func1.replace('d[0]', str(d[0]))
            func1 = func1.replace('d[1]', str(d[1]))
            func1 = func1.replace('a(x)', str(mu * penalty[1]))
            res = round(eval(func1), roun)
        case 'p':
            ar = []
            ar.append(2 * x[0] + x[1] - 2)
            ar.append(-x[0] + 1)
            res = ar[0] + ar[1]
    return res

def printRess(k, x, fx, j, d, y, lamb, y1):
    if k == 1 and j == 1:
        print(f'{"":-^86}')
        print(f'| k  |        xk       |  j  |    dj   |        yj       |  labmj  |       yj+1      |')
        print(f'{"":-^86}')
    if j == 1:
        print(f'|{k:^4}| {x[0]: >7.4f}:{x[1]: >7.4f} | {j: >3.1f} | {d[0]: >3.1f}:{d[1]:.1f} | {x[0]: >7.4f}:{x[1]: >7.4f} | {lamb: >7.4f} | {y1[0]: >7.4f}:{y1[1]: >7.4f} |')
    elif j == 2:
        print(f'|{k:^4}| {fx: >15.4f} | {j: >3.1f} | {d[0]: >3.1f}:{d[1]:.1f} | {y[0]: >7.4f}:{y[1]: >7.4f} | {lamb: >7.4f} | {y1[0]: >7.4f}:{y1[1]: >7.4f} |')
    print(f'{"":-^86}')

def countPoint(lamb, y, d):
    y1 = []
    for i in range(len(y)):
        y1.append(round(y[i] + (lamb * (d[i])), roun))
    return y1

class iter_gaus:
    def __init__(self, k, rng=100):
        self.k = k
        self.rng = rng

    def newPoint(self, x):
        j = 1
        self.x = x
        self.fx = getFoo(x=x, goal='f')
        d = vectors[j-1]
        self.lamb1 = getGoldenRatioRes(d, self.x, self.rng)
        results['goldenRes'] = []
        self.y = countPoint(self.lamb1[1], x, d)
        self.fy = getFoo(x=self.y, goal='f') 
        printRess(self.k, x, self.fx, j, d, x, self.lamb1[1], self.y)

        j += 1
        d = vectors[j-1]
        self.lamb2 = getGoldenRatioRes(d, self.y, self.rng)
        results['goldenRes'] = []
        self.y1 = countPoint(self.lamb2[1], self.y, d)
        self.fy1 = self.lamb2[1]
        printRess(self.k, self.x, self.fx, j, d, self.y, self.lamb2[1], self.y1)

        ang = math.sqrt((self.y1[0] - self.x[0])**2 + ((self.y1[1] - self.x[1])**2))
        return ang

def chooseFoo():
    foos = [
        '(x1**2 - x2**2 + x1 * x2 - x1 + 2 * x2)',
        '((x1 - x2)**2 + (x2 - 2)**2)',
        '(9 * (x1**2) + 16 * (x2**2) - 90 * x1 - 128 * x2)',
        '((x1 - 2)**4 + (x1 - (2 * x2))**2 + a(x))',
        '((x1**2 + x2**2) + a(x))'
    ]
    print('Choose number of function:')
    for i in range(len(foos)):
        print(f'{i+1}. {foos[i]}')
    choise = int(input('Enter number: ')) 
    return [foos[choise - 1], choise]

def countByChoise(x1, x2, choise):
    match choise:
        case 1:
            res = (x1**2 - x2**2 + x1 * x2 - x1 + 2 * x2)
        case 2:
            res = ((x1 - x2)**2 + (x2 - 2)**2)
        case 3:
            res = (9 * (x1**2) + 16 * (x2**2) - 90 * x1 - 128 * x2)
        case 4:
            res = ((x1 - 2)**4 + (x1 - (2 * x2))**2)
        case 5:
            res = (x1**2 + x2**2)
    return res

def getPoints(ar):
    x_val = []
    y_val = []
    x_val.append(x1)
    y_val.append(x2)
    for i in range(len(ar)):
        x_val.append(ar[i].y[0])
        x_val.append(ar[i].y1[0])
        y_val.append(ar[i].y[1])
        y_val.append(ar[i].y1[1])

    return x_val, y_val

def buildPlot(arr, rng):
    rng = 1
    px = arr[-1].y1[0]
    py = arr[-1].y1[1]

    X_AX = np.arange(px - rng, px + rng, 0.1)
    Y_AX = np.arange(py - rng, py + rng, 0.1)
    X, Y = np.meshgrid(X_AX, Y_AX)
    counted_points = getPoints(arr)
    plt.plot(counted_points[0], counted_points[1], 'bo', linestyle='--')
    plt.plot(px, py, marker='o', markersize=12, markeredgecolor='red', markerfacecolor='yellow')

    C = plt.contour(X, Y, countByChoise(X, Y, choise), 8, colors='black')
    plt.contourf(X, Y, countByChoise(X, Y, choise), 8)
    plt.clabel(C, inline=1, fontsize=10)
    plt.colorbar()

    plt.show()


gaus_res = []
rng = 10
roun = 6
vectors = [
    [1, 0],
    [0, 1]
]
k = 0
ang = 10
foon, choise = chooseFoo()
x1 = int(input('Enter x1: ')) # 0
x2 = int(input('Enter x2: ')) # 3
x = [x1, x2]
eps = float(input('Enter eps: ')) # 0.01

mu = 10000 
beta = 5 

while True:
    k += 1
    gaus_res.append(iter_gaus(k, rng))
    foo = '1'
    if k == 1: 
        penalty = getGoldenRatioRes([1,1], x, rng)
    else:
        penalty = getGoldenRatioRes([1,1], gaus_res[k-1].y1, rng)

    foo = '2'
    results['goldenRes'] = [] 
    if k != 1: 
        ang = gaus_res[k-1].newPoint(gaus_res[k-2].y1)
    else:
        ang = gaus_res[k-1].newPoint(x)

    foo = '1'
    penalty = getGoldenRatioRes([1,1], gaus_res[k-1].y1, rng)

    foo = '2'
    results['goldenRes'] = [] 

    print(countByChoise(gaus_res[k-1].y1[0], gaus_res[k-1].y1[1], choise), eps, penalty[1])
    if penalty[1] < eps:
        break 
    else: 
        mu = mu * beta

buildPlot(gaus_res, rng)
