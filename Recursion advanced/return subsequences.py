#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def subsequences(s):
    if len(s)==0:
        output=[]
        output.append("")
        return output
    smallOutput=subsequences(s[1:])
    
    output=[]
    for sub in smallOutput:
        output.append(sub)
        
    for sub in smallOutput:
        output.append(s[0]+sub)
        
    return output


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)





