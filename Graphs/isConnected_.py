#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class built:
    def __init__(self,vertex):
        self.vertex=vertex
        self.matrix=[[0 for x in range(vertex)] for y in range(vertex)]
        self.visited=[False for x in range(vertex)]
    
    def addv(self,a,b):   
        self.matrix[a][b]=1
        self.matrix[b][a]=1

    def fp(self,p1,p2):

        self.visited[p1]=True
        for ele in range(self.vertex):
            if self.visited[ele]==False and self.matrix[p1][ele]==1:
               
                a=self.fp(ele,p2)
        for i in range(self.vertex):
            if self.visited[i]==False:
                return False
           
        return True
           
       
       
       
l=[int(x) for x in input().split()]
x=l[0]
y=l[1]
z=built(x)
for i in range(y):
    l1=[int(x) for x in input().split()]
    a,b=l1[0],l1[1]
    z.addv(a,b)
k=z.fp(a,b)
if k:
    print('true')
else:
    print('false')
  

