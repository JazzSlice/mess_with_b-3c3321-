import math

eps = 0.1
target = 0.1
a = -7
b = -3

a1 = a
b1 = b

dixotomicRes = []
goldenRes = []
fiboRes = []

class iter_info:
    def __init__(self, k):
        self.k = k

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

def printRes (arr):
    print("|      a      |      b      |    lambda    |     mu     |   F(lambda)   |     F(mu)    |")
    print("----------------------------------------------------------------------------------------")
    for i in range(len(arr)):
        obj = arr[i]
        print("|{: >13.4f}|{: >13.4f}|{: >14.4f}|{: >12.4f}|{: >15.4f}|{: >14.4f}|".format(obj.a, obj.b, obj.Lambda, obj.Mu, obj.FLamb, obj.FMu))

def getGoldenRatioRes (a, b):
    k = 0
    teta = ((math.sqrt(5) - 1) / 2)
    
    while b - a > target:
        k += 1
        Lambda = (a + (1 - teta) * (b - a))
        Mu = (a + teta * (b - a))
        FLamb = getFooRes(Lambda, 1)
        FMu = getFooRes(Mu, 1)
        if FLamb > FMu:
            a = Lambda
            b = b
            Lambda = Mu
            Mu = (a + teta * (b - a))
            FMu = getFooRes(Mu, 1)
        else:
            a = a
            b = Mu
            Mu = Lambda
            Lambda = (a - (1 - teta) * (b - a))
            FMu = getFooRes(Mu, 1)

    i2target = (math.log((b1 - a1) / target) / math.log(teta))

    print("__________________GOLDEN_RATIO_RESULT_________________")
    print("x in bounds of                 [{:}:{:}]\nResult is: {: >37}".format(a, b, ((a + b) / 2)))
    print('Iterations calculated: {: >9} \nIterations for target: {: >9}'.format(k, -math.floor(i2target)))
    print('Length by calculated values: {: >10.5} \nLength by formula: {: >17.5}'.format(b-a, target/(b1-a1)))

def getDixotomicRes (a, b):
    k = 0
    dixotomicRes.append(iter_info(k))
    arr = dixotomicRes[k]
    arr.a = a
    arr.b = b
    while arr.b - arr.a > target:
        dixotomicRes.append(iter_info(k + 1))
        arr1 = dixotomicRes[k+1]
        arr.Lambda = (((arr.a + arr.b) / 2) - eps)
        arr.Mu = (((arr.a + arr.b) / 2) + eps)
        arr.FLamb = getFooRes(arr.Lambda, 1)
        arr.FMu = getFooRes(arr.Mu, 1)
        print(dixotomicRes)
        if arr.FLamb > arr.FMu:
            arr1.a = arr.Mu
            arr1.b = arr.b
        else:
            arr1.a = arr.a
            arr1.b = arr.Lambda
        k += 1
        arr = dixotomicRes[k]
    arr.Lambda = (((arr.a + arr.b) / 2) - eps)
    arr.Mu = (((arr.a + arr.b) / 2) + eps)
    arr.FLamb = getFooRes(arr.Lambda, 1)
    arr.FMu = getFooRes(arr.Mu, 1)

    i2target = (math.log((b1 - a1) / target) / math.log(2))
    
    print("___________________DIXOTOMIC_RESULT___________________")
    print("x in bounds of                 [{:}:{:}]\nResult is: {: >27}".format(arr.a, arr.b, ((arr.a + arr.b) / 2)))
    print('Iterations calculated: {: >9} \nIterations for target: {: >9}'.format(k, math.trunc(i2target)))
    print('Length by calculated values: {: >8.5} \nLength by formula: {: >17.5}'.format(arr.b-arr.a, target/(b1-a1)))
    printRes(dixotomicRes)

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
