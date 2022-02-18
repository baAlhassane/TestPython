# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:08:55 2022

@author: DVEEC
"""


def colred(inpout):
    prod=1;
    #if(inpout.isnumeric()):
    x=[int(n) for n in str(inpout)]
    xp=x[:];
    n=len(x)
    for i in range(n-1):
      x.append(x[i]*x[i+1])
    for e in xp:
        prod*=e;
    x.append(prod)   
    return x;

    
def is_colored(inpout):
    x=colred(inpout)[:]
    print(x)
    n=len(x)
    for i in range(n):
        for j in range(n):
            if( (x[i]==x[j])and (i!=j)  ):
                return False
    return True;         
    
    
    
    
if __name__ == "__main__":
    inpout1=263
    inpout2=236
    inpout3=2532
    l=colred(inpout1)
    print(l)
    print("---------------------")
    b1=is_colored(inpout1)
    print(b1)
    print("---------------------")
    b2=is_colored(inpout2)
    print(b2)
    print("---------------------")
    b3=is_colored(inpout3)
    print(b3)
    
    