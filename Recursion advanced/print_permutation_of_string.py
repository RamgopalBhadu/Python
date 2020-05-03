#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def permutations(s,output):
    
    length=len(s)
    if length==0:
        print(output)
        return
    for i in range(0,length):
        permutations(s[0:i]+s[i+1:],output+s[i])

        
def printPermutations(s):
    #Implement Your Code Here
	permutations(s,"")

string = input()
printPermutations(string)





