#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    # Please add your code here
    if len(s)==0 or len(s)==1:
        return s
    if s[0]==s[1]:
        smalloutput=removeConsecutiveDuplicates(s[1:])
        return smalloutput
    else:
        smalloutput=removeConsecutiveDuplicates(s[1:])
        return s[0]+smalloutput
    pass

# Main
s = input().strip()
print(removeConsecutiveDuplicates(s))

