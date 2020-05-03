#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def getString(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return " "

def keypad(n,outputSoFar):
    if n==0:
        print(outputSoFar)
        return
    
    smallerNumber=n//10
    lastdigit=n%10
    
    optionsForLastDigit=getString(lastdigit)
    for c in optionsForLastDigit:
        smallOutput=c+outputSoFar
        keypad(smallerNumber,smallOutput)
        
    

    

n = int(input())
keypad(n,"")

