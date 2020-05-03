#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def subsequences(s,o):
    if len(s)==0:
        print(o)
        return
    subsequences(s[1:],o)
    subsequences(s[1:],o+s[0])

        
        
string = input()
ans = subsequences(string,"")

