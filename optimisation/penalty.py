import math
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

teta = ((math.sqrt(5) - 1) / 2)
target = 0.1
results = {
    'goldenRes': []
}

class iter_info:
    def __init__(self, k):
        self.k = k + 1
    def getInfo(self):
        print(f'|{self.k:^4}|{self.a: >13.4f}|{self.b: >13.4f}|{self.Lambda: >14.4f}|{self.Mu: >12.4f}|{self.FLamb: >15.4f}|{self.FMu: >14.4f}|')
    def calc(self, v, y1, goldFlag):
            match goldFlag:
                case 0:
                    self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
                    self.Mu = (self.a + teta * (self.b - self.a))
                case 1:
                    self.Mu = (self.a + teta * (self.b - self.a))
                case 2:
                    self.Lambda = (self.a + (1 - teta) * (self.b - self.a))

            self.FLamb = getFoo(self.Lambda, v, y1)
            self.FMu = getFoo(self.Mu, v, y1)


def getGoldenRatioRes (vect, y1, rng):
    ka, fCalc = 0, 0
    goldFlag = 0
    res = results['goldenRes']
    res.append(iter_info(ka))
    arr = res[ka]
    
    arr.a, arr.b = min(-rng, rng), max(-rng, rng)
    fCalc += 2
    arr.calc(vect, y1, goldFlag)
    while abs(arr.b - arr.a) > eps:
        res.append(iter_info(ka + 1))
        arr1 = res[ka + 1]
        arr.calc(vect, y1, goldFlag)
        fCalc += 0
        foper = arr.FLamb
        soper = arr.FMu
        if foper > soper:
            goldFlag = 1
            fCalc += 1
            arr1.a, arr1.b = arr.Lambda, arr.b
            arr1.Lambda = arr.Mu
            arr1.Mu = (arr1.a + teta * (arr1.b - arr1.a))
            arr1.calc(vect, y1, goldFlag)
        else:
            goldFlag = 2
            fCalc += 1
            arr1.a, arr1.b = arr.a, arr.Mu
            arr1.Mu = arr.Lambda
            arr1.Lambda = (arr1.a + (1 - teta) * (arr1.b - arr1.a))
            arr1.calc(vect, y1, goldFlag)
        goldFlag = 0
        ka += 1
        arr = res[ka]
    
    return [round((abs(arr.a - arr.b)) / 2, roun), arr.Lambda]

def getFoo(lamb, d, x):
    x1, x2 = x[0] + (lamb * d[0]), x[1] + (lamb * d[1])
    return countByChoise(x1, x2)

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
        self.fx = x[0]**2 + x[1]**2 + mu * countPenal(x)
        d = vectors[j-1]
        self.lamb1 = getGoldenRatioRes(d, self.x, self.rng)
        results['goldenRes'] = []
        self.y = countPoint(self.lamb1[1], x, d)
        self.fy = self.y[0]**2 + self.y[1]**2 + mu * countPenal(self.y)

        j += 1
        d = vectors[j-1]
        self.lamb2 = getGoldenRatioRes(d, self.y, self.rng)
        results['goldenRes'] = []
        self.y1 = countPoint(self.lamb2[1], self.y, d)
        self.fy1 = self.y1[0]**2 + self.y1[1]**2 + mu * countPenal(self.y1)

        ang = math.sqrt((self.y1[0] - self.x[0])**2 + ((self.y1[1] - self.x[1])**2))
        return ang

def countByChoise(x1, x2):
    x = [x1, x2]
    if finish_flag:
        return (x1**2 + x2**2)
    else:
        return ((x1**2 + x2**2)) + countPenal(x) * mu

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
    rng = 5
    px = arr[-1].y1[0]
    py = arr[-1].y1[1]

    X_AX = np.arange(px - rng, px + rng + 0.1, 0.1)
    Y_AX = np.arange(py - rng, py + rng + 0.1, 0.1)
    X, Y = np.meshgrid(X_AX, Y_AX)

    counted_points = getPoints(arr)
    plt.plot(counted_points[0], counted_points[1], 'bo', linestyle='--')
    plt.plot(px, py, marker='o', markersize=12, markeredgecolor='red', markerfacecolor='yellow')

    C = plt.contour(X, Y, countByChoise(X, Y), 8, colors='black')
    plt.contourf(X, Y, countByChoise(X, Y), 8)
    plt.clabel(C, inline=1, fontsize=10)
    plt.colorbar()

    plt.show()

def countPenal(pen):
    a = max((2 * pen[0] + pen[1] - 2), 0)
    b = max((-pen[1] + 1), 0)   
    return (a**2+b**2)
    
finish_flag = 0
gaus_res = []
rng = 1
roun = 4
vectors = [
    [1, 0],
    [0, 1]
]
k = 0
ang = 10

x1 = int(input('Enter x1: ')) # 0
x2 = int(input('Enter x2: ')) # 3
x = [x1, x2]
eps = float(input('Enter eps: ')) # 0.01

mu = 100
beta = 10

while True:
    k += 1
    gaus_res.append(iter_gaus(k, rng))
    
    if k != 1:
        ang = gaus_res[-1].newPoint(gaus_res[-2].y1)
    else:
        penal = countPenal(x) * mu
        ang = gaus_res[-1].newPoint(x)
        
    fres = gaus_res[-1].y1[0]**2 + gaus_res[-1].y1[1]**2

    if k == 1:
        print('| k   |   mu   |           xk+1          |   f(xk)   |    alfa   |    omega   |  mu_alfa   |')
        print(f'{"":-^92}')
    print(f'|{k:^4} | {round(mu, roun): >6} | {gaus_res[-1].y1[0]: >11}:{gaus_res[-1].y1[1]: >11} | {round(fres, roun): >9} | {round(countPenal(gaus_res[-1].y1), roun): >9} | {round(fres + round(countPenal(gaus_res[-1].y1) * mu, roun)): > 10} | {round(countPenal(gaus_res[-1].y1) * mu, roun): >11}|')
    print(f'{"":-^92}')

    if countPenal(gaus_res[-1].y1) * mu < eps:
        break 
    else: 
        if k == 1:
            mu = 0.1
        mu *= beta
finish_flag = 1
# print(gaus_res[-1].y1, round(fres, roun), countPenal(gaus_res[-1].y1) * mu)
print(f'Optimal value is {gaus_res[-1].y1} in {eps} range\nPenalty in dot = {round(countPenal(gaus_res[-1].y1) * mu, roun)}\nAssistant function in dot = {round(gaus_res[-1].fy1, roun)}')
buildPlot(gaus_res, rng)