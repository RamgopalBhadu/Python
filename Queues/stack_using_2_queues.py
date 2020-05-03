#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import queue
class StackUsingQueues:
    
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.curr_size=0
        
    def push(self,x):
        self.curr_size += 1
  
        # Push x first in empty q2  
        self.q2.put(x)  
  
        # Push all the remaining  
        # elements in q1 to q2.  
        while (not self.q1.empty()): 
            self.q2.put(self.q1.queue[0])  
            self.q1.get()
            
        while (not self.q2.empty()): 
            self.q1.put(self.q2.queue[0])  
            self.q2.get()
        

    def pop(self):
        if (self.q1.empty()):  
            return
        data=self.q1.get()  
        self.curr_size -= 1
        return data
    
    def top(self):
        if (self.q1.empty()): 
            return -1
        return self.q1.queue[0] 
       
    def getSize(self):
        return self.curr_size 
    
s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        li = []
        while s.q1.qsize() !=0:
            li.append(s.q1.get())
        print(*li[::-1])    
            
    i+=1






