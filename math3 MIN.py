import math
import numpy as np

eps = 0.1
L_dlina = 0.1
a = -7
b = -3 
k = 1

a1 = -7
b1 = -3 

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