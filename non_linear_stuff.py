import math

eps = 0.1
target = 0.1
a = -7
b = -3

a1 = a
b1 = b
teta = ((math.sqrt(5) - 1) / 2)
goldFlag = 0

dixotomicRes = []
goldenRes = []
fiboRes = []

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
        self.FLamb = getFooRes(self.Lambda, 1)
        self.FMu = getFooRes(self.Mu, 1)

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
            i2target = (math.log((b1 - a1) / target) / math.log(teta))
            print("_____________GOLDEN_RATIO_RESULT_____________")
        
    print("x in bounds of{: >23.4f}:{:.4f}\nResult is: {: >26.4f}".format(obj.a, obj.b, ((obj.a + obj.b) / 2)))
    print('Iterations calculated: {: >9} \nIterations for target: {: >9}'.format(len(arr), math.trunc(i2target)))
    print('Length by calculated values: {: >8.5} \nLength by formula: {: >17.5}'.format(obj.b-obj.a, target/(b1-a1)))
    print("----------------------------------------------------------------------------------------")
    print("|      a      |      b      |    lambda    |     mu     |   F(lambda)   |     F(mu)    |")
    print("----------------------------------------------------------------------------------------")
    for i in range(len(arr)):
        arr[i].getInfo()
        
def getGoldenRatioRes (a, b):
    k = 0
    method = 'gold'
    goldenRes.append(iter_info(k))
    arr = goldenRes[k]
    arr.a, arr.b = a, b
    while b - a > target:
        goldenRes.append(iter_info(k + 1))
        arr1 = goldenRes[k + 1]
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
        arr = goldenRes[k]
        a, b = arr.a, arr.b
    arr.calc(method)
    printRes(goldenRes, method)

def getDixotomicRes (a, b):
    k = 0
    method = 'dixo'
    dixotomicRes.append(iter_info(k))
    arr = dixotomicRes[k]
    arr.a, arr.b = a, b
    while b - a > target:
        dixotomicRes.append(iter_info(k + 1))
        arr1 = dixotomicRes[k + 1]
        arr.calc(method)
        if arr.FLamb > arr.FMu:
            arr1.a, arr1.b = arr.Mu, arr.b
        else:
            arr1.a, arr1.b = arr.a, arr.Lambda
        k += 1
        arr = dixotomicRes[k]
        a, b = arr.a, arr.b
    arr.calc(method)
    printRes(dixotomicRes, method)

# def getFiboRes (a, b):
#     k, i, n = 0
#     i2target = ((b1 - a1) / target)
#     while i < i2target:
#         n += 1
#         i = getFiboNum(n)

#     while k < n:
#         k += 1
#         Lambda = (a + (getFiboNum(n - k - 1) / getFiboNum(n - k + 1) * (b - a)))
#         Mu = (a + (getFiboNum(n - k) / getFiboNum(n - k + 1) * (b - a)))
#         FLamb = getFooRes(Lambda, 1)
#         FMu = getFooRes(Mu, 1)
#         if FLamb > FMu:
#             if k != (n - 2):
#                 a = Lambda
#                 Lambda = Mu
#                 Mu = (a + (getFiboNum(n - k - 1) / getFiboNum(n - k) * (b - a)))
#                 FMu = getFooRes(Mu, 1)
#             else:
#                 break
#         else:
#             if k != (n - 2):
#                 b = Mu
#                 Mu = Lambda
#                 Lambda = (a + (getFiboNum(n - k - 2) / getFiboNum(n - k) * (b - a)))
#                 FLamb = getFooRes(Lambda, 1)
#             else:
#                 break
#     Lambda = 

      

getGoldenRatioRes (a, b)
getDixotomicRes (a, b)
