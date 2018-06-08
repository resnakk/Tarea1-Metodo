# -*- coding: utf-8 -*-
"""
Created on Sun May 27 21:55:08 2018

@author: Chico_NOTE_2018
"""
#=========================  P3 =============================
#A
import numpy as np
import time 
def relax(MatrizA, VectorB, Error,w):
    
    n = len(VectorB)
    XK = np.zeros([n,1], float)
    XK1 = np.zeros([n,1], float)
    cont = 1
    o = 1
    while True:
        if o == 1 :
            o += 1
            continue
        else:
            f = bool(np.linalg.norm(XK1 - XK) < Error)#np.linalg.norm(MatrizA*XK1 - VectorB) <= Error*np.linalg.norm(VectorB))
            #print np.linalg.norm(MatrizA*XK1 - VectorB) , Error*np.linalg.norm(VectorB), MatrizA[0,0]*XK1[0,0], VectorB[0,0] 
            #No use este criterio de salida por que no salia nunca de la primera iteracion            
            if  f == True:
                return [XK1, cont]
                print cont
                break
            else:
                for i in range(1, n + 1 ):
                        sum1 = 0
                        if i == 1:
                            continue
                        else:
                            for j in range(1, i):
                                sum1 += MatrizA[i - 1,j - 1]*XK1[i - 1, 0]
                        sum2 = 0
                        for k in range(i + 1, n + 1):
                            sum2 += MatrizA[i - 1, k - 1]*XK[k - 1, 0]
                        
                        top = w*(-sum1 - sum2 + VectorB[i - 1,0])
                        c = (1 - w)*XK[i - 1, 0]
                        XK1[i - 1, 0] = top/MatrizA[i - 1, i - 1] + c
                o += 1
                XK = XK1
                cont += 1
                print cont
        o = 1         
                    
            
#B)1)
ws =    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
XAproxs = []
NIteracioness = []
for n in range(100,1001):
    MatrizA = np.zeros((n,n))
    VectorB = np.zeros([n,1],float)
    for i in range(1, n + 1):
        VectorB[i - 1 ,0] = 1.0/i
        for j in range(1, n + 1):
                if i == j:
                    MatrizA[i - 1, j - 1] = 20 + i
                else:
                    MatrizA[i - 1, j - 1] = float((-1)**(i + j))/float(i + j)
    #print MatrizA
    for omega in range(len(ws)):
        XAprox , NIteraciones = relax(MatrizA, VectorB, 10**(-10),ws[omega])
        XAproxs.append(XAprox)
        NIteracioness.append(NIteraciones)         
#1)
for i in range(len(ws)):
    print 'b)1)\nPara w = ', ws[i], '\nx = ',XAproxs[i] 
            
            
            
            
            
            
            
            
            
            
            
    