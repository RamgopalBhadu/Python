#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def subset(arr,k):
    n=len(arr)
    if(n==1):
        if(arr[0]==k):
            output=[[k]]
            return output
        else:
            output=[]
            return output
        
    output1=subset(arr[:-1],k)
    output2=subset(arr[:-1],k-arr[-1])
    for lst in output2:
        lst.append(arr[-1])
    if arr[-1]==k:
        output2.append([k])
    return output1+output2

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=subset(arr,k)
for i in ans:
    for num in i:
        print(num,end=' ')
    print()

