# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:17:55 2022
"""

from first_part.src import exercise_one

#test_output = "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n11\nThree\n13\n14\nThreeFive\n16\n17\nThree\n19\nFive\nThree\n22\n23\nThree\nFive\n26\nThree\n28\n29\nThreeFive\n31\n32\nThree\n34\nFive\nThree\n37\n38\nThree\nFive\n41\nThree\n43\n44\nThreeFive\n46\n47\nThree\n49\nFive\nThree\n52\n53\nThree\nFive\n56\nThree\n58\n59\nThreeFive\n61\n62\nThree\n64\nFive\nThree\n67\n68\nThree\nFive\n71\nThree\n73\n74\nThreeFive\n76\n77\nThree\n79\nFive\nThree\n82\n83\nThree\nFive\n86\nThree\n88\n89\nThreeFive\n91\n92\nThree\n94\nFive\nThree\n97\n98\nThree\nFive\n"


def split_string(chaine ,sep):
    return chaine.split(sep)

def is_multtiple_3(x):
    sum=0;
    if(x.isnumeric()):
        for c in x:
            n = int(c)
            sum+=n
        return sum%3==0
    else :
       return False;
            
    
            
def is_multtiple_5(x):
    if(x.isnumeric()):
       c= int(x[-1])
       return( c==0 or c==5 )
            

def is_multtiple_3_and_5(x):
    return is_multtiple_3(x) and is_multtiple_5(x)
    
def print_mult_3_and_5(inpout):
    numbers=split_string(inpout,"\n")
    for number in numbers:
        if(is_multtiple_3_and_5(number)):
           print("ThreeFive")
           continue
        if(is_multtiple_3(number)):
            print("Three")
            continue
        if(is_multtiple_5(number)):
            print("Five")
            continue
        print(number)
            
            
    

def test_first_exercise(capsys):
    exercise_one()
    captured = capsys.readouterr()
    assert captured.out == test_output



if __name__ == "__main__":
    chaine = "alhas et alhous" 
    chaine_list=split_string(chaine,"et")
    print(chaine_list)
    x="335"
    print(is_multtiple_3(x))
    print(is_multtiple_5(x))
    inpout="1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16"
    print_mult_3_and_5(inpout)
    
    
    
    