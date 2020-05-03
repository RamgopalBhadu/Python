#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def palindrome(string,s,e):
    if len(string)==0:
        return 'true'
    if s==e:
        return 'true'
    if (string[s] != string[e]) : 
        return 'false'
    if (s < e + 1) : 
        return palindrome(string, s + 1, e - 1); 
  
    return 'true'


string=input()  
l=len(string)
e=l-1
z=palindrome(string,0,e)
print(z)

