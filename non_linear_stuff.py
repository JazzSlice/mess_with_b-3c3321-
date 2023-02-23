import math
#import numpy as np

eps = 0.1
L_dlina = 0.1
a = -7
b = -3 
k = 1

a1 = a
b1 = b


def getDixotomicResult (a, b, k, a1, b1, L_dlina, eps):

    while b - a > L_dlina: 
        
        Lambda = (a + b)/2 - eps 
        Mu = (a + b)/2 + eps 
        
        FKLamb = (4*(Lambda**2-2*Lambda-8)*(Lambda**2-9))/(Lambda**2-Lambda**4)
        FKMu = (4*(Mu**2-2*Mu-8)*(Mu**2-9))/(Mu**2-Mu**4)

        
        print ("кол-во итераций: ",k)
        print ("а и б: ",a, b)
        print ("в функциях лямбва и мю: ",FKLamb, FKMu)

        if FKLamb < FKMu:
            if b - Mu > eps :
                
                a = a
                b = Mu 
            else:
                break 
        else:
            if a - Lambda > eps :
                
                a = Lambda
                b = b  
            else:
                break 
            
        k += 1



        if k == 20: 
            break


    else: 
        print ("complete")
    #    k += 1
    #    print (a, b)
        print ("real KKK:", k)

    DlinaUnn = ((1/2**k)*(b-a)) + (2*eps)*(1-(1/2**k))

    print ("длина неопределенности: ", DlinaUnn)

    pupu = (b1-a1)/DlinaUnn

    print ("pupu is ", pupu)

    NNN = math.log(pupu)/math.log(2)

    print ("кол-во итераций NNN", NNN)

def getGoldenRationResult(a, b, k, a1, b1, L_dlina, eps):
    teta = ((math.sqrt(5) - 1) / 2)
    teta_res = teta
    Lambda = (a + (1 - teta) * (b - a))
    Mu = (a + teta * (b - a))
    FKLamb = (4 * (Lambda**2 - 2 * Lambda - 8) * (Lambda**2 - 9)) / (Lambda**2 - Lambda**4)
    FKMu = (4 * (Mu**2 - 2 * Mu - 8) * (Mu**2 - 9)) / (Mu**2 - Mu**4)
    result = 0
    while (b - a > L_dlina):
        if FKLamb > FKMu:
            a_act = a
            b_act = b
            a = Lambda
            Lambda = Mu
            Mu = a + (teta * (b - a))
            FKMu = (4*(Mu**2-2*Mu-8)*(Mu**2-9))/(Mu**2-Mu**4)
        else:
            a_act = a
            b_act = b
            b = Mu
            Mu = Lambda
            Lambda = a - (1 - teta) * (b - a)
            FKLamb = (4*(Lambda**2-2*Lambda-8)*(Lambda**2-9))/(Lambda**2-Lambda**4)
        teta_res = teta
        teta = ((b - a) / (b_act - a_act))
    else:
        result = ((a + b) / 2)
        k += 1
        NNN = (math.log((b1 - a1) / L_dlina) / math.log((math.sqrt(5) - 1) / 2))
        print('Result is: {: >43} \nIterations calculated: {: >16} \nIterations by formula: {: >16}'.format(result, k, math.trunc(NNN)))
        print('Length by calculated values: {: >16.5} \nLength by formula: {: >26.5}'.format(b-a, teta_res))
        print('a = {:}, b = {:}'.format(a, b))
# def getFiboResult (a, b, k, a1, b1, L_dlina, eps):
#    Lambda = (a + ((getFiboNum((b - a) - k - 1)) / (getFiboNum((b - a) - k + 1)) * (b - a)))
#    Mu = (a + ((getFiboNum((b - a) - k)) / (getFiboNum((b - a) - k + 1)) * (b - a))
#    NNN = ((b - a) / getFiboNum(b - a)
#    FKMu = (4*(Mu**2-2*Mu-8)*(Mu**2-9))/(Mu**2-Mu**4)
#    FKLamb = (4*(Lambda**2-2*Lambda-8)*(Lambda**2-9))/(Lambda**2-Lambda**4)

getDixotomicResult (a, b, k, a1, b1, L_dlina, eps)
getGoldenRationResult (a, b, k, a1, b1, L_dlina, eps)
