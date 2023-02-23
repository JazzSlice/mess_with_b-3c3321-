import math

eps = 0.1
target = 0.1
a = -7
b = -3 

a1 = a
b1 = b

fibo_arr = [1, 1]

def getFiboNum (k):
    i = k - 1
    if fibo_arr[i] != 1:
        fibo_arr[i] = fibo_arr[i - 1] + fibo_arr[i - 2]
    return fibo_arr[i]

def getFooRes (x, num):
    if num == 1:
        x = (4 * ((x**2 - 2*x - 8) * (x**2 - 9)) / (x**2 - x**4))
    else:
        x = (x**3 + 2*(x**2) - x + 2)
    return x


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

    print("_______GOLDEN_RATIO_RESULT_______")
    print("x in bounds of [{:}:{:}]\nResult is: {: >37}".format(a, b, ((a + b) / 2)))
    print('Iterations calculated: {: >9} \nIterations for target: {: >9}'.format(k, -math.floor(i2target)))
    print('Length by calculated values: {: >10.5} \nLength by formula: {: >17.5}'.format(b-a, target/(b1-a1)))

def getDixotomicRes (a, b):
    k = 0
    while b - a > target:
        k += 1
        Lambda = (((a + b) / 2) - eps)
        Mu = (((a + b) / 2) + eps)
        FLamb = getFooRes(Lambda, 1)
        FMu = getFooRes(Mu, 1)
        if FLamb > FMu:
            a = Mu
        else:
            b = Lambda
    k += 1
    i2target = (math.log((b1 - a1) / target) / math.log(2))
    
    print("________DIXOTOMIC_RESULT_________")
    print("x in bounds of [{:}:{:}]\nResult is: {: >27}".format(a, b, ((a + b) / 2)))
    print('Iterations calculated: {: >9} \nIterations for target: {: >9}'.format(k, math.floor(i2target)))
    print('Length by calculated values: {: >8.5} \nLength by formula: {: >17.5}'.format(b-a, eps/(b1-a1)))


getGoldenRatioRes (a, b)
getDixotomicRes (a, b)
