#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def totalWays(n):
    if n<3:
        return n
    elif n == 3:
        return 4
    return totalWays(n-3)+totalWays(n-2)+totalWays(n-1)



n=int(input())
a=totalWays(n)
print(a)

