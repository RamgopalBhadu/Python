#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import queue
def reverseQueue(queue):
    Stack = []  
    while (not queue.empty()):  
        Stack.append(queue.queue[0])  
        queue.get() 
    while (len(Stack) != 0):  
        queue.put(Stack[-1])  
        Stack.pop() 
    
from sys import setrecursionlimit
setrecursionlimit(11000)
li = [int(ele) for ele in (input().split()[1:])]
q1 = queue.Queue()
for ele in li:
    q1.put(ele)
reverseQueue(q1)
while(q1.empty() is False):
    print(q1.get(),end= ' ')





