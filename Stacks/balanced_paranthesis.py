#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def checkBalanced(expr):
    s=[]
    for char in expr:
        if char in'[{(':
            s.append(char)
        elif char is ')':
            if(not s or s[-1]!='('):
                return False
            s.pop()
        elif char is ']':
            if(not s or s[-1]!='['):
                return False
            s.pop()
        elif char is '}':
            if(not s or s[-1]!='{'):
                return False
            s.pop()
    if(not s):
        return True
    else:
        return False
### Implement your code here

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

