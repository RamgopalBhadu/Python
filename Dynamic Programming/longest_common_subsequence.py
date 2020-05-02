#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def lcsDP(s1, s2):
    n=len(s1)
    m=len(s2)
    dp=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]

s1 =input().strip()
s2 =input().strip()
print(lcsDP(s1, s2))

