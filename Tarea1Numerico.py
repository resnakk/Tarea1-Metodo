# -*- coding: utf-8 -*-
"""
Created on Sun May 27 21:55:08 2018

@author: Chico_NOTE_2018
"""
#=========================  P3 =============================
#A
import numpy as np
def relax(MatrizA, VectorB, Error,w):
    n = len(VectorB)
    D = np.diag(MatrizA)
    E = np.tril(MatrizA)
    F = np.triu(MatrizA)
    print D
    print E
    print F
    a = raw_input('')
    D1 = np.linalg.inv(D)
    I = np.identity(n)
    Mr = np.linalg.inv(1 + w*(D1*E))*((1 - w)*I - w*(D1*F))
    ValoresP , VectoresP = np.linalg.eig(Mr)
    ro = max(abs(ValoresP))
    if ro >= 1:
        return [[],0]
    else:
        XK = np.zeros([n,1],float) #Parto del vector 0, y pongo float para q sepa q se pueden decimales
        i = 1
        while True:
            XK1 = np.dot(Mr,XK)
            if np.linalg.norm(MatrizA,XK - VectorB) <= Error*np.linalg.norm(VectorB):
                i += 1
                continue
            else:
                return [XK1,i]
#B)1)
ws =    [0.1, 1.9]
XAproxs = []
NIteracioness = []
for omega in range(2):
    for n in range(100,1001):
        MatrizA = np.zeros((n,n))
        VectorB = np.zeros([n,1],float)
        for i in range(1, n + 1):
            VectorB[i - 1 ,0] = 1.0/i
            for j in range(n):
                    if i == j:
                        MatrizA[i - 1, j - 1] = 20 + i
                    else:
                        MatrizA[i - 1, j - 1] = ((-1)**(i + j))/(i + j)          
        #aqui caga la wea, en la primera it 
        #print MatrizA,VectorB
        XAprox = relax(MatrizA, VectorB, 10**(-10),ws[omega])
        NIteraciones = relax(MatrizA, VectorB, 10**(-10),ws[omega])          
        XAproxs.append(XAprox)
        NIteracioness.append(NIteraciones)    
        
#1)

print 'b)1)\nPara w = ', ws[i], '\nx = ',XAproxs[i] 
            
            
            
            
            
            
            
            
            
            
            
    