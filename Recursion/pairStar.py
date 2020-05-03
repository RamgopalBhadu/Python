#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def  pairstar(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]==s[1]:
        smalloutput=pairstar(s[1:])
        return s[0]+'*'+smalloutput
    else:
        smalloutput=pairstar(s[1:])
        return s[0]+smalloutput
    
    
s=input().strip()
print(pairstar(s))

