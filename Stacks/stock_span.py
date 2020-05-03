#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def stockSpan(price, n): 
      
    # Span value of first day is always 1 
    S = [None] * n
    S[0] = 1
  
    # Calculate span value of remaining days by linearly  
    # checking previous days 
    for i in range(1, n, 1): 
        S[i] = 1   # Initialize span value 
  
        # Traverse left while the next element on left is 
        # smaller than price[i] 
        j = i - 1
        while (j>= 0) and (price[i] > price[j]) : 
                       S[i] += 1
                       j -= 1
    return S

    

    
    
#### Implement Your Code Here

n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')




