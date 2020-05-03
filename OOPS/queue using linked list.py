#!/usr/bin/env python
# coding: utf-8

# In[ ]:



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class QueueUsingLL:
  
### Implement These Functions Here    
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
        
    def enqueue(self,data):
        newNode=Node(data)
        if self.__head is None:
            self.__head=newNode
            self.__tail=newNode
        else:    
            self.__tail.next=newNode
        self.__tail=newNode
        self.__count=self.__count+1
        
    def dequeue(self):
        if self.__head is None:
            return
        data=self.__head.data
        self.__head=self.__head.next
        self.__count=self.__count-1
        return data
    
    def front(self):
        if self.__head is None:
            return
        data=self.__head.data
        return data
    
    def isEmpty(self):
        return getSize()==0
    
    def getSize(self):
        return self.__count

    
q = QueueUsingLL()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        q.enqueue(li[i+1])
        i+=1
    elif choice == 2:
        ans = q.dequeue()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = q.front()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(q.getSize())
    elif choice == 5:
        if(q.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1






