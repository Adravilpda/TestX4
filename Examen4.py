# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
Author: Mahesh Venkitachalam

"""
import numpy as np
def sigmoid(x, derivada=False):
    if derivada:
        return x*(1-x)
    return 1/(1+np.exp(-x))

X=np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])

y=np.array([ [0] , [0] , [0] , [1] ])


capas=3
conexiones=4
salidas=1

syn0=3*np.random.random((capas,conexiones))-1
syn1=3*np.random.random((conexiones,salidas))-1

entrenamiento=1000
error=100

for j in range(entrenamiento):
    
    layer0=X
    layer1=sigmoid(np.dot(layer0,syn0))
    
    layer2=sigmoid(np.dot(layer1,syn1))
 
    layer2_error=y-layer2
    
    if(j%error)==0:
        print(np.mean(np.abs(layer2_error)))
        
    layer2_delta=layer2_error*sigmoid(layer2,derivada=True)
    
    layer1_error=layer2_delta.dot(syn1.T)
    
    layer1_delta=layer1_error*sigmoid(layer1,derivada=True)
    
    syn1+=layer1.T.dot(layer2_delta)
    syn0+=layer0.T.dot(layer1_delta)
print("Salida")
print(layer2)
