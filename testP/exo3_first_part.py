# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:42:00 2022

@author: DVEEC
"""

def calculate(liste):
    sum=0;
    if(type(liste)==list):
        for l in liste:
            if(type(l)==str):
                try:
                    s=float(l)
                    sum+=s
                except:
                    continue
        sum=int(sum)        
        return sum    
    else:
       return False         
    
if __name__ == "__main__":
    l=['4', '3', '-2']
    s=calculate(l)
    print(s)
    l1=calculate(453) #➞ False
    print(l1)
    l2=['nothing', 3, '8', 2, '1']
    s1=calculate(l2) #➞ 9
    print(s1)
    s2=calculate('54')# ➞ False
    print(s2)