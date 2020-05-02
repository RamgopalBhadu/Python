#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
import sys
def minCost(cost,m,n):
    dp=[[sys.maxsize for j in range(n+1)] for i in range(m+1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j==n-1:
                dp[i][j]=cost[i][j]
            else:
                ans1=dp[i+1][j]
                ans2=dp[i][j+1]
                ans3=dp[i+1][j+1]
                dp[i][j]=cost[i][j]+min(ans1,ans2,ans3)
    return dp[0][0]


m,n=[int(i) for i in input().strip().split(' ')]
cost=[]
for i in range(m):
    cost.append([int(i) for i in input().strip().split(' ')])
ans=minCost(cost,m,n)
print(ans)

