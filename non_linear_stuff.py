import math
import numpy as np
import matplotlib.pyplot as plt

eps = float(input('Введите эпсилон: ')) # 0.001
target = float(input('Введите конечный интервал неопределенности: ')) # 0.01
a = int(input('Введите границу "a": ')) # -1
b = int(input('Введите границу "b": ')) # 4

a1 = a
b1 = b
foo = input('Введите номер целевой функции: ') # '2'
teta = ((math.sqrt(5) - 1) / 2)
goldFlag = 0
# file = open('test.pdf', 'a', encoding="utf-8")

results = {
    'dixotomicRes': [],
    'goldenRes': [],
    'fiboRes': []
}


class iter_info:
    def __init__(self, k):
        self.k = k + 1
    def getInfo(self):
        print(f'|{self.k:^4}|{self.a: >13.4f}|{self.b: >13.4f}|{self.Lambda: >14.4f}|{self.Mu: >12.4f}|{self.FLamb: >15.4f}|{self.FMu: >14.4f}|')
    def calc(self, method):
        match method:
            case 'dixo':
                self.Lambda = (((self.a + self.b) / 2) - eps)
                self.Mu = (((self.a + self.b) / 2) + eps)
            case 'gold':
                match goldFlag:
                    case 0:
                        self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
                        self.Mu = (self.a + teta * (self.b - self.a))
                    case 1:
                        self.Mu = (self.a + teta * (self.b - self.a))
                    case 2:
                        self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
            case 'fibo':
                self.Lambda = (self.a + getFiboNum(self.n - self.k - 3) / getFiboNum(self.n - self.k -1))

        self.FLamb = getFooRes(self.Lambda, foo)
        self.FMu = getFooRes(self.Mu, foo)

def getFiboNum (k):
    a, b = 0, 1
    for i in range(k):
        a, b = b, a + b
    return b

def getFooRes (x, num):
    match num:
        case '1':
            x = (4 * ((x**2 - 2*x - 8) * (x**2 - 9)) / (x**2 - x**4))
        case '2':
            x = (x**3 + 2*(x**2) - x + 2)
    return x

def printRes (arr, method, fCalc):
    obj = arr[(len(arr) - 1)]
    match method:
        case 'dixo':
            txt = 'DIXOTOMIC_RESULT'
            i2target = (np.log((b1 - a1) / target) / np.log(2))
            print(f"{txt:_^93}")
        case 'gold':
            txt = 'GOLDEN_RATIO_RESULT'
            i2target = (np.log((b1 - a1) / target) / np.log(teta))# could use //
            print(f"{txt:_^93}")
        case 'fibo':
            txt = 'FIBONACCI_RESULT'
            i2target = ((b1 - a1) / target)
            i, n = 0, 0
            while i < i2target:
                n += 1
                i = getFiboNum(n)
            i2target = n
            print(f"{txt:_^93}")

    print(f'x in bounds of{obj.a: >23.4f}:{obj.b:.4f}\nResult is: {(obj.a + obj.b) / 2: >26.4f}')
    print(f'Iterations calculated: {len(arr): >9}\nFoo Calculated: {fCalc: >16}')# \nIterations for target: {: >9}'.format(len(arr), math.floor(i2target)))
    print('Length by calculated values: {: >7.3f} \nLength by formula: {: >17.3f}'.format(obj.b-obj.a, target/(b1-a1)))
    print(f'{"":-^93}')
    print("| k  |      a      |      b      |    lambda    |     mu     |   F(lambda)   |     F(mu)    |")
    print(f'{"":-^93}')
    for i in range(len(arr)):
        arr[i].getInfo()
    if obj.a > obj.b:
        n = obj.a
        obj.a = obj.b
        obj.b = n
    # resd, resg, resf = results['dixotomicRes'], results['goldenRes'], results['fiboRes']
    # a = max(resd[len(resd) - 1].a, resg[len(resg) - 1].a, resf[len(resf) - 1].a)
    # b = min(resd[len(resd) - 1].b, resg[len(resg) - 1].b, resf[len(resf) - 1].b)
    z = abs((obj.a + obj.b) / 2)
    # x = np.arange(a1, b1, eps)
    x = np.arange(obj.a - eps, obj.b + eps, eps)
    # plt.axvline(x = a1)
    # plt.axvline(x = b1)
    plt.axvline(x = obj.a, color = 'black')
    plt.axvline(x = obj.b, color = 'black')
    
    y = getFooRes(x, foo)
    # match foo:
    #     case '1':
    #         y = (4 * ((x**2 - 2*x - 8) * (x**2 - 9)) / (x**2 - x**4))
    #     case '2':
    #         y = (x**3 + 2*(x**2) - x + 2)
    plt.plot(x, y, color='blue')
    plt.show()

def getDixotomicRes (a, b):
    k, fCalc = 0, 0
    method = 'dixo'
    res = results['dixotomicRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b = a, b
    while b - a > target:
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        arr.calc(method)
        fCalc += 2
        match foo:
            case '1':
                foper = arr.FLamb
                soper = arr.FMu
            case '2':
                foper = arr.FMu
                soper = arr.FLamb
        if foper > soper:
            arr1.a, arr1.b = arr.Mu, arr.b
        else:
            arr1.a, arr1.b = arr.a, arr.Lambda
        k += 1
        arr = res[k]
        a, b = arr.a, arr.b
    arr.a, arr.b = arr.b,arr.a
    arr.calc(method)
    fCalc += 2
    printRes(res, method, fCalc)

def getFiboRes (a, b):
    k, i, n, fCalc = 0, 0, 0, 0
    i2target = ((b1 - a1) / target)
    while i < i2target:
        n += 1
        i = getFiboNum(n)

    method = 'fibo'
    res = results['fiboRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b, arr.n = a, b, n
    arr.Lambda = (arr.a + ((getFiboNum(arr.n - arr.k - 1)) / getFiboNum(arr.n - arr.k + 1)) * (arr.b - arr.a))
    arr.Mu = (arr.a + (getFiboNum(arr.n -  arr.k) / getFiboNum(arr.n - arr.k + 1)) * (arr.b - arr.a))
    arr.FLamb = getFooRes(arr.Lambda, foo)
    arr.FMu = getFooRes(arr.Mu, foo)
    fCalc += 2
    for i in range(n):
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        match foo:
            case '1':
                foper = arr.FLamb
                soper = arr.FMu
            case '2':
                foper = arr.FMu
                soper = arr.FLamb
        if foper > soper:
            arr1.a, arr1.b, arr1.Lambda, arr1.n = arr.Lambda, arr.b, arr.Mu, arr.n
            arr1.Mu = (arr1.a + (getFiboNum(arr1.n - arr.k - 1)) / (getFiboNum(arr1.n - arr.k)) * (arr1.b - arr1.a))
            if (arr.k) != (arr.n - 2):
                k += 1
                arr = res[k]
                arr.FMu = getFooRes(arr.Mu, foo)
                arr.FLamb = getFooRes(arr.Lambda, foo)
                fCalc += 2
            else:
                break
        else:
            arr1.a, arr1.b, arr1.Mu, arr1.n = arr.a, arr.Mu, arr.Lambda, arr.n
            arr1.Lambda = (arr1.a + ((getFiboNum(arr1.n - arr.k - 2)) / getFiboNum(arr.n - arr.k)) * (arr1.b - arr1.a))
            if (arr.k) != (arr.n - 2):
                k += 1
                arr = res[k]
                arr.FLamb = getFooRes(arr.Lambda, foo)
                arr.FMu = getFooRes(arr.Mu, foo)
                fCalc += 2
            else:
                break
    arra = res[len(res) - 1]
    arrp = res[len(res) - 2]
    arra.Lambda = arrp.Lambda
    arra.Mu = (arra.Lambda + eps)
    arra.FLamb = getFooRes(arra.Lambda, foo)
    arra.FMu = getFooRes(arra.Mu, foo)
    if arra.FLamb > arra.FMu:
        arra.a, arra.b = arra.Lambda, arrp.b
    else:
        arra.a, arra.b = arrp.a, arra.Mu
    printRes(res, method, fCalc)

def getGoldenRatioRes (a, b):
    k, fCalc = 0, 0
    method = 'gold'
    res = results['goldenRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b = a, b
    while b - a > target:
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        arr.calc(method)
        fCalc += 2
        match foo:
            case '1':
                foper = arr.FLamb
                soper = arr.FMu
            case '2':
                foper = arr.FMu
                soper = arr.FLamb
        if foper > soper:
            goldFlag = 1
            fCalc += 1
            arr1.a, arr1.b = arr.Lambda, arr.b
            arr1.Lambda = arr.Mu
            arr1.calc(method)
        else:
            goldFlag = 2
            fCalc += 1
            arr1.a, arr1.b = arr.a, arr.Mu
            arr1.Mu = arr.Lambda
            arr1.calc(method)
        goldFlag = 0
        k += 1
        arr = res[k]
        a, b = arr.a, arr.b
    arr.calc(method)
    printRes(res, method, fCalc)

getDixotomicRes (a, b)
getGoldenRatioRes(a, b)
getFiboRes(a, b)

# file.close()
