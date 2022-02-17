# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 01:13:50 2022

"""

def number_letter_in_word(word):
    d=dict()
    for letter in word:
        if(letter in d):
            d[letter]+=1
        else:
            d[letter]=1
      
    return d
            
        
def anagrams(word, liste):
    n=len(word)
    l=[]
    for word1 in liste:
        m=len(word1)
        if(m!=n):
            continue;
        d1=number_letter_in_word(word)
        d2=number_letter_in_word(word1)
        i=0
        for k2 in d2:
           if(k2 in d1):
               if(d1[k2]==d2[k2]):
                   i+=d1[k2];
                   continue;
        if(i!=m):
            continue
        else:
            l.append(word1)
               
    return l           
    
    
if __name__ == "__main__":
    l1= ['aabb', 'abcd', 'bbaa', 'dada']
    l1_anagrams=anagrams('abba', l1) #=> ['aabb', 'bbaa'] 
    print(l1_anagrams)   
    print("-----------------------------------------")
    l2=['crazer', 'carer', 'racar', 'caers', 'racer']
    l2_anagrams= anagrams('racer', l2) #=> ['carer', 'racer']
    print(l2_anagrams) 
    a=number_letter_in_word("crazer")
    print(a)
    print("-----------------------------------------")
    l3=['lazing', 'lazy',  'lacer']
    l3_anagrams=anagrams('laser',l3 )# => []
    print(l3_anagrams)
   
              
            