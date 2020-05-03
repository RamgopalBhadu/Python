#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def string_to_integer(string,si):
    l=len(string)
    if si==0:
        return 0
       
    
    return int(string[si-1])+10*string_to_integer(string,si-1)

    
    
string=input().strip()

output=(string_to_integer(string,len(string))-1)+1
print(output)

