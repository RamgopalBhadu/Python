#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import sys,math
def minStepsTo1(n,dp):
    if n==0:
        return 0
    sys.setrecursionlimit(10000)
    ans=sys.maxsize
    root=int(math.sqrt(n))
    for i in range(1,root+1):
        if dp[n-i*i]==-1:
            small=minStepsTo1(n-i*i,dp)
            dp[n-i*i]=small
            currAns=1+small
        else:
            currAns=1+dp[n-i*i]
        ans=min(ans,currAns)
    return ans
        

    
n = int(input())
dp=[-1 for i in range(n+1)]
ans = minStepsTo1(n,dp)
print(ans)





