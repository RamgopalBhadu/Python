#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def returnSubset(li):
    n=len(li)
    if len(li)<=0:
        output=[[]]
        #output.append(" ")
        return output
    
    output=returnSubset(li[:n-1])
    outputLen=len(output)
    
    for i in range(outputLen):
        output.append(output[i].copy())
        output[outputLen+i].append(li[len(li)-1])
        
    #for sub in smallOutput:
        #output.append([sub,li[0]])
        
    return output
    
    
n=int(input())
li=[int(i) for i in input().strip().split()]
ans=returnSubset(li)
for i in ans:
    for num in i:
        print(num,end=' ')
    print()

