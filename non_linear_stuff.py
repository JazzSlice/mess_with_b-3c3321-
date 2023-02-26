import math

eps = 0.01
target = 0.01
a = -1
b = 4

a1 = a
b1 = b
foo = 2
teta = ((math.sqrt(5) - 1) / 2)
goldFlag = 0

results = {
    'dixotomicRes': [],
    'goldenRes': [],
    'fiboRes': []
}

class iter_info:
    def __init__(self, k):
        self.k = k
    def getInfo(self):
        print("|{: >13.4f}|{: >13.4f}|{: >14.4f}|{: >12.4f}|{: >15.4f}|{: >14.4f}|".format(self.a, self.b, self.Lambda, self.Mu, self.FLamb, self.FMu))
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
    return a

def getFooRes (x, num):
    match num:
        case 1:
            x = (4 * ((x**2 - 2*x - 8) * (x**2 - 9)) / (x**2 - x**4))
        case 2:
            x = (x**3 + 2*(x**2) - x + 2)
    return x

def printRes (arr, method):
    obj = arr[(len(arr) - 1)]
    match method:
        case 'dixo':
            i2target = (math.log((b1 - a1) / target) / math.log(2))
            print("______________DIXOTOMIC_RESULT_______________")
        case 'gold':
            i2target = (math.log((b1 - a1) / target) / math.log(teta)) # could use //
            print("_____________GOLDEN_RATIO_RESULT_____________")
        case 'fibo':
            i2target = ((b1 - a1) / target)
            print("___________FIBONACCI_RATIO_RESULT____________")
        
    print("x in bounds of{: >23.4f}:{:.4f}\nResult is: {: >26.4f}".format(obj.a, obj.b, ((obj.a + obj.b) / 2)))
    print('Iterations calculated: {: >9} \nIterations for target: {: >9}'.format(len(arr), -math.floor(i2target)))
    print('Length by calculated values: {: >8.5} \nLength by formula: {: >17.5}'.format(obj.b-obj.a, target/(b1-a1)))
    print("----------------------------------------------------------------------------------------")
    print("|      a      |      b      |    lambda    |     mu     |   F(lambda)   |     F(mu)    |")
    print("----------------------------------------------------------------------------------------")
    for i in range(len(arr)):
        arr[i].getInfo()
        
def getGoldenRatioRes (a, b):
    k = 0
    method = 'gold'
    res = results['goldenRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b = a, b
    while b - a > target:
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        arr.calc(method)
        if arr.FLamb > arr.FMu:
            goldFlag = 1
            arr1.a, arr1.b = arr.Lambda, arr.b
            arr1.Lambda = arr.Mu
            arr1.calc(method)
        else:
            goldFlag = 2
            arr1.a, arr1.b = arr.a, arr.Mu
            arr1.Mu = arr.Lambda
            arr1.calc(method)
        k += 1
        arr = res[k]
        a, b = arr.a, arr.b
    arr.calc(method)
    printRes(res, method)

def getDixotomicRes (a, b):
    k = 0
    method = 'dixo'
    res = results['dixotomicRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b = a, b
    while b - a > target:
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        arr.calc(method)
        if arr.FLamb > arr.FMu:
            arr1.a, arr1.b = arr.Mu, arr.b
        else:
            arr1.a, arr1.b = arr.a, arr.Lambda
        k += 1
        arr = res[k]
        a, b = arr.a, arr.b
    arr.calc(method)
    printRes(res, method)

def getFiboRes (a, b):
    k, i, n = 0, 0, 0
    i2target = ((b1 - a1) / target)
    while i < i2target:
        n += 1
        i = getFiboNum(n)

    method = 'fibo'
    res = results['fiboRes']
    res.append(iter_info(k))
    arr = res[k]
    arr.a, arr.b, arr.n = a, b, n
    arr.Lambda = (arr.a + ((getFiboNum(arr.n - 2)) / getFiboNum(arr.n)) * (arr.b - arr.a))
    arr.Mu = (arr.a + (getFiboNum(arr.n -1) / getFiboNum(arr.n)) * (arr.b - arr.a))
    arr.FLamb = getFooRes(arr.Lambda, foo)
    arr.FMu = getFooRes(arr.Mu, foo)
    for i in range(n):
        res.append(iter_info(k + 1))
        arr1 = res[k + 1]
        if arr.FLamb > arr.FMu:
            arr1.a, arr1.b, arr1.Lambda, arr1.n = arr.Lambda, arr.b, arr.Mu, arr.n
            arr1.Mu = (arr1.a + (getFiboNum(arr1.n - k - 1)) / (getFiboNum(arr1.n - k)) * (arr1.b - arr1.a))
            if arr1.k != (arr1.n - 2):
                k += 1
                arr = res[k]
                arr.FMu = getFooRes(arr.Mu, foo)
                arr.FLamb = getFooRes(arr.Lambda, foo)
            else:
                break
        else:
            arr1.a, arr1.b, arr1.Mu, arr1.n = arr.a, arr.Mu, arr.Lambda, arr.n
            arr1.Lambda = (arr1.a + ((getFiboNum(arr1.n - k)) / getFiboNum(arr.n - arr.k + 1)) * (arr1.b - arr1.a))
            if arr1.k != (arr1.n - 2):
                k += 1
                arr = res[k]
                arr.FLamb = getFooRes(arr.Lambda, foo)
                arr.FMu = getFooRes(arr.Mu, foo)
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
    printRes(res, method)

getGoldenRatioRes (a, b)
getDixotomicRes (a, b)
getFiboRes(a, b)
