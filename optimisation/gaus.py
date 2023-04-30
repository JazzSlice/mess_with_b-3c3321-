import math
import numpy as np
import matplotlib.pyplot as plt

oper = '0'
foo = '2'
teta = ((math.sqrt(5) - 1) / 2)
target = 0.1
# eps = 0.1
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
    # z = ((obj.a + obj.b) / 2)
    # x = np.arange(obj.a, obj.b, eps)
    # plt.axvline(x = obj.a, color = 'black')
    # plt.axvline(x = obj.b, color = 'black')
    # plt.axvline(x = z, color = 'red')
    # y = (obj.FLamb)
    # # y = round(getFooRes((obj.a + obj.b) / 2, foo, v, y1), 8)
    # plt.plot(x, y, color='blue')
    # plt.show()

def getFooRes (x, num, v, y1):
    match num:
        case '1':
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
        case '2':
            if oper == '0':
                x2 = y1[1]
                y = y1[0]
                # x1 = y
                x =  (((y + (x * v)) - x2)**2 + (x2 - 2)**2)
            elif oper == '1':
                x1 = y1[0]
                y = y1[1]
                # x2 = y
                x = ((x1 - (y + (x * v)))**2 + ((y + (x * v)) - 2)**2)
    return x

def evalFoo(lamb, foo, d, x):
    lamb = lamb # later use in .replace magic method
    foo = foo
    # func = '(((-x1)**2) - (x2**2) + (x1 * x2) - x1 + (2 * x2))'
    # func = '((x1 - x2)**2 + (x2 - 2)**2)'
    func = '(9 * (x1**2) + 16 * (x2**2) - 90 * x1 - 128 * x2)'
    x1 = '(x[0] + (lamb * d[0]))'
    x2 = '(x[1] + (lamb * d[1]))'
    func = func.replace('x1', x1)
    func = func.replace('x2', x2)
    func = func.replace('x[0]', str(x[0]))
    func = func.replace('x[1]', str(x[1]))
    func = func.replace('d[0]', str(d[0]))
    func = func.replace('d[1]', str(d[1]))
    # func = func.replace('lamb', str(lamb))
    return round(eval(func), 4)

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
            
        self.FLamb = evalFoo(self.Lambda, foo, v, y1)
        self.FMu = evalFoo(self.Mu, foo, v, y1)
        
        
        # self.FLamb = getFooRes(self.Lambda, foo)
        # self.FMu = getFooRes(self.Mu, foo)

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
                foper = arr.FLamb
                soper = arr.FMu
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
        a, b = arr.a, arr.b
    arr.calc(method, vect, y1, goldFlag)
    # printRes(res, method, fCalc, vect, y1)
    
    return [round((abs(arr.a - arr.b)) / 2, 4), arr.Lambda]

def getFoo(x):
    x1 = x[0]
    x2 = x[1]
    # res = (((-x1)**2) - (x2**2) + (x1 * x2) - x1 + (2 * x2))
    # res = ((x1 - x2)**2 + (x2 - 2)**2)
    res = (9 * (x1**2) + 16 * (x2**2) - 90 * x1 - 128 * x2)
    return res

def printRess(k, x, fx, j, d, y, lamb, y1):
    print(f'{"":-^86}')
    if j == 1:
        print(f'|{k:^4}| {x[0]: >7.4f}:{x[1]: >7.4f} | {j: >3.1f} | {d[0]: >3.1f}:{d[1]:.1f} | {y[0]: >7.4f}:{y[1]: >7.4f} | {lamb: >7.4f} | {y1[0]: >7.4f}:{y1[1]: >7.4f} |')
    elif j == 2:
        print(f'|{k:^4}| {fx: >15.4f} | {j: >3.1f} | {d[0]: >3.1f}:{d[1]:.1f} | {y[0]: >7.4f}:{y[1]: >7.4f} | {lamb: >7.4f} | {y1[0]: >7.4f}:{y1[1]: >7.4f} |')
    # print(f'{"":-^86}')

def countPoint(lamb, y, d):
    y1 = []
    for i in range(len(y)):
        y1.append(round(y[i] + (lamb * (d[i])), 4))
    return y1


print(f'| k  |        xk       |  j  |    dj   |        yj       |  labmj  |       yj+1      |')
rng = 5
# Step 0
x1 = 5
x2 = -3
x = [x1, x2]
vectors = {
    '0': [1, 0],
    '1': [0, 1]
}
k = 1
j = 0
eps = 0.001
# Step 1
j += 1
d = vectors[f'{j-1}']
y1 = [x1, x2]

fx = getFoo(x)
lamb1 = getGoldenRatioRes([1, 0], x, rng)
results['goldenRes'] = []
y = countPoint(lamb1[1], x, [1, 0])
fy = getFoo(x)
printRess(k, x, fx, j, [1, 0], y1, lamb1[1], y)

j += 1
lamb2 = getGoldenRatioRes([0, 1], y, rng)
results['goldenRes'] = []
y1 = countPoint(lamb2[1], y, [0, 1])
fy1 = getFoo(y1)
printRess(k, x, fx, j, [0, 1], y1, lamb2[1], y)

ang = math.sqrt((y1[0] - x[0])**2 + ((y1[1] - x[1])**2))
# ang = abs(y1[0] - x[0]) + abs(y1[1] - x[1])

j = 0

while ang > eps:
    x = y1
    k += 1
    j += 1
    d = [1, 0]
    lamb1 = getGoldenRatioRes(d, x, rng)
    results['goldenRes'] = []
    y = countPoint(lamb1[1], x, d)
    fl = getFoo(x) 
    printRess(k, x, fl, j, d, y1, lamb1[1], y)

    j += 1
    d = [0, 1]
    lamb2 = getGoldenRatioRes(d, y, rng)
    results['goldenRes'] = []
    y1 = countPoint(lamb2[1], y, d)
    fl = lamb2[1]
    printRess(k, x, fl, j, d, y, lamb2[1], y1)

    ang = math.sqrt((y1[0] - x[0])**2 + ((y1[1] - x[1])**2))
    print(getFoo([x1, x2]), '\n', getFoo(y), getFoo(y1))
    print(ang)
    j = 0
