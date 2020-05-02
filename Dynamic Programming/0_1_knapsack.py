#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def knapsackBF(wt, values,W):
    n=len(values)
    dp=[[0 for j in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1+W):
            if j<wt[i-1]:
                ans=dp[i-1][j]
            else:
                ans1= values[i-1] + dp[i-1][j-wt[i-1]]
                ans2= dp[i-1][j]
                ans=max(ans1,ans2)
            dp[i][j]=ans
    return dp[n][W]

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
weights=list(int(i) for i in input().strip().split(' '))
values=list(int(i) for i in input().strip().split(' '))
maxWeight=int(input())
print(knapsackBF(weights, values, maxWeight))
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

