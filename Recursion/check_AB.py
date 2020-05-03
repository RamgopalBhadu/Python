#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def CheckAB(str):
    if(len(str)==0):
        return True
    if(str[0]=='a'):
        if(len(str[1:])>1 and str[1:3]=='bb'):
            return CheckAB(str[3:])
        else:
            return CheckAB(str[1:])
    else:
        return False
str=input()
if(CheckAB(str)):
    print("true")
else:
    print("false")

