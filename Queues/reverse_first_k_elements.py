#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue 
def reverseFirstK(Queue,k):
    if (Queue.empty() == True or
             k > Queue.qsize()):  
        return
    if (k <= 0):
        return
  
    Stack = [] 
  
    # put the first K elements  
    # into a Stack 
    for i in range(k): 
        Stack.append(Queue.queue[0])  
        Queue.get() 
  
    # Enqueue the contents of stack  
    # at the back of the queue 
    while (len(Stack) != 0 ):  
        Queue.put(Stack[-1])  
        Stack.pop() 
  
    # Remove the remaining elements and  
    # enqueue them at the end of the Queue 
    for i in range(Queue.qsize() - k): 
        Queue.put(Queue.queue[0])  
        Queue.get()
#Implement Your Code Here     

        
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k) 
while(q.qsize()>0):
	print(q.get())
	n-=1

