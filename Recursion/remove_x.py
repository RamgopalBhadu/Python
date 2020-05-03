#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem: Remove x from string
def removeX(string): 
    l=len(string)
    if l==0:
        return string
    smallstring=string[1:]
    smallOutput = removeX(smallstring)
    if string[0]=='x':
        return smallOutput
    else:
        return string[0]+smallOutput
    pass

# Main
string = input()

print(removeX(string))

