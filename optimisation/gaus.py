import math

eps = 0.001
target = 0.1
foo = '1'
goldFlag = 0
teta = ((math.sqrt(5) - 1) / 2)
j = 0

vectors = {
    '1': [1, 0],
    '2': [0, 1],
}
x1 = [0, 0]
x2 = x1

results = {'goldenRes': []}
    
def getFooRes (x1, x2, num):
    match num:
        case '1': # x1[0] += v_lamb * vector[0]
            x = ((-x1) ** 2 - (x2 ** 2) + (x1 * x2) - x1 + (2 * x2))
        case '2':
            x = (x**3 + 2*(x**2) - x + 2)
    return x

class iter_info:
    def __init__(self, k):
        self.k = k + 1
    def getInfo(self):
        print(f'|{self.k:^4}|{self.a: >13.4f}|{self.b: >13.4f}|{self.Lambda: >14.4f}|{self.Mu: >12.4f}|{self.FLamb: >15.4f}|{self.FMu: >14.4f}|')
    def calc(self, method):
        match goldFlag:
            case 0:
                self.Lambda = (self.a + (1 - teta) * (self.b - self.a))
                self.Mu = (self.a + teta * (self.b - self.a))
            case 1:
                self.Mu = (self.a + teta * (self.b - self.a))
            case 2:
                self.Lambda = (self.a + (1 - teta) * (self.b - self.a))

        self.FLamb = getFooRes(x1[0], self.Lambda, foo)
        self.FMu = getFooRes(x1[0], self.Mu, foo)

def getGoldenRatioRes (a, b):
    k, fCalc = 0, 0
    method = 'gold'
    res = results['goldenRes']
    res.append(iter_info(k))
    arr = res[k]
    if a > b:
        arr.a, arr.b = b, a
    else:
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
                foper = arr.FLamb
                soper = arr.FMu
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
    arr.a, arr.b = a, b
    arr.calc(method)
    x = ((arr.a + arr.b) / 2)
    return [x, getFooRes(x, x, foo)]
#######################################

for j in range(len(vectors)):
    vector = vectors[f'{j + 1}']
    x2[j] = getFooRes(x1[j], x1[j] + vector[0], foo) # нашли оптимальное значение для 1 шага
    # x2[j+1] = getFooRes(x1[1], x1[1] + vector[1], foo)
x2x = getGoldenRatioRes(x1[0], x2[1])
print(x2[0], x2[1])
print(x2x[0], x2x[1])



#######################################