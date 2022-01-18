# -*- coding: utf-8 -*-

__author__ = "Fabian Hormigo Pereila"
__copyright__ = "Copyright (C) 2021 Fabian Hormigo Pereila"
__license__ = "Public Domain"
__version__ = "1.0"
#fuction for celular wall on off
def celularopen(k_1,k_0,N,n):
    import numpy as np 
    
    r1=np.random.uniform(0,1,len(n))
    r2=np.random.uniform(0,1,len(n))
    
    tau=np.log(1/r1)/(k_1*(1+N-n)+k_0*(n+1))
    A=np.array(k_1*(N-n+1))
    B=np.array(k_1*(N-n+1)+k_0*(n+1))
    C=A/B
    w_=1-C
    v=[]
    for k in range(len(n)):
        wk=w_[k]
        r2k=r2[k]
        
        if wk>r2k:
            a=[-1]
            v=np.append(v,a)
        else:
            b=[1]
            v=np.append(v,b)
    return [v,tau]
            
      
        
    
    

