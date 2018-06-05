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
    #print n
    Diagonal = np.diag(MatrizA)
    D = np.zeros((n,n))   
    for i in range(n):
        for j in range(n):
            if i == j:            
                D[i,j] = Diagonal[i]     
    L = np.tril(MatrizA)
    U = np.triu(MatrizA)
    #print F
    #D1 = np.linalg.inv(D)
    #I = np.identity(n)
    #Mr = 
    XK = np.zeros([n,1],float) #Parto del vector 0, y pongo float para q sepa q se pueden decimales
    #cw = (w*np.linalg.inv(D - w*F))*VectorB
    #print D-w*F    
    i = 1
    while True:
        XK1 = w*np.linalg.inv(L + D)*(VectorB - U*XK) + (1 - w)*XK
        cond = np.linalg.norm(MatrizA*XK - VectorB) 
        er =  Error*np.linalg.norm(VectorB)
        #print XK
        print cond, er 
        #time.sleep(0.5)
        if cond >= er:
            i += 1
            XK = XK1
            print cond, er
            continue
        else:
            return [XK1,i]
            
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
            
            
            
            
            
            
            
            
            
            
            
    