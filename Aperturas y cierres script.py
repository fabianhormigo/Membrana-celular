# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 00:37:16 2021

@author: fabia
"""

_author__ = "Fabian Hormigo Pereila"
__copyright__ = "Copyright (C) 2021 Fabian Hormigo Pereila"
__license__ = "Public Domain"
__version__ = "1.0"
import numpy as np 
from celularwall import celularopen as cell
from matplotlib import pyplot as plt 

#generador apertura y cierre estudio de los datos

tracks=1300
#inputs
k_0=0.1
k_1=0.1
    #number of total cells
N=100
    #number of initial open cells for each truck(vectorized fun)
n=30*np.ones(tracks)



acumuladortime=np.zeros([tracks,1000])

acumuladorn=np.zeros([tracks,1000])
acumuladormedio=[]
acumediocuadrado=[]


for k in range(1000):
    
    [deltan,t_out]=cell(k_0,k_1,N,n)
    
    acumuladorn[:,k]=n+deltan
    
    acumuladortime[:,k]=t_out
    
    n=n+deltan
    
    ncuadrado=n*n
    
    valoremedion=np.median(n)
    
    valoremedioncuadrado=np.median(ncuadrado)
    
    acumuladormedio=np.append(acumuladormedio,valoremedion)
    
    acumediocuadrado=np.append(acumediocuadrado,valoremedioncuadrado)
    
#ploteo histograma y valores medios
neq=n
n_medio=acumuladormedio
n_medio_cuadrado=acumediocuadrado

#plot valor medio y valor medio cuadrado t
plt.figure(1)
plt.plot(n_medio)
plt.ylabel('<n>')
plt.xlabel('Time')
plt.savefig('Valorn.png')

plt.figure(2)
plt.plot(n_medio_cuadrado)
plt.ylabel('<n^2>')
plt.xlabel('Time')
plt.savefig('Valormedio_cuadrado_n.png')

#Histograma
HistogramaS=plt.figure(3)

gamma=plt.hist(neq,bins=50)
plt.xlabel('Número de membranas celulares abiertas')

plt.savefig('HistogramaMembrana1.png')

    
    
    
    
    
    
    
    
    
    
   
    
   
  
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
    


