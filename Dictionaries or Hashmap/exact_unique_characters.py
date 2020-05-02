#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def uniqueChars(string):
    # Please add your code here
    li=list(string)
    d={}
    for w in li:
        if w in d:
            d[w]=d[w]+1
        else:
            print(w,end='')
            d[w]=1
        
    pass

# Main
string = input()
uniqueChars(string)

