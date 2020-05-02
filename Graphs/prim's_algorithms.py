#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
import sys
import queue
class graph:
    def __init__(self,nvertices):
        self.nvertices=nvertices
        self.adjmatrix=[[0 for i in range(nvertices)] for j in range(nvertices)]
    def addedge(self,v1,v2,wt):
        self.adjmatrix[v1][v2]=wt
        self.adjmatrix[v2][v1]=wt
    def removeedge(self):
        if self.containsedge(v1,v2) is False:
            return
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0
    def containsedge(self,v1,v2):
        if self.adjmatrix[v1][v2]>0:
            return True
        else:
            return False
    def __str__(self):
        return str(self.adjmatrix)
    def __bfs(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while q.empty() is False:
            u=q.get()
            print(u,end=" ")
            for i in range(self.nvertices):
                if self.adjmatrix[u][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
    def bfs(self):
        visited=[False for i in range(self.nvertices)]
        for i in range(self.nvertices):
            if visited[i] is False:
                self.__bfs(i,visited)
    
    def get_minVertex(self,visited,weight):
        min_vertex=-1
        for i in range(self.nvertices):
            if(visited[i] is False and (min_vertex==-1 or weight[min_vertex]>weight[i])):
                min_vertex=i
        return min_vertex
        
    def prims(self):
        visited=[False for i in range(self.nvertices)]
        parent=[-1 for i in range(self.nvertices)]
        weight=[sys.maxsize for i in range(self.nvertices)]
        weight[0]=0
        for i in range(self.nvertices-1):
            min_vertex= self.get_minVertex(visited,weight)
            visited[min_vertex]=True
            
            for j in range(self.nvertices):
                if self.adjmatrix[min_vertex][j]>0 and visited[j]==False:
                    if (weight[j]>self.adjmatrix[min_vertex][j]):
                        weight[j]=self.adjmatrix[min_vertex][j]
                        parent[j]=min_vertex
        
        for i in range(1,self.nvertices):
            if i<parent[i]:
                print(str(i)+" "+str(parent[i])+" "+str(weight[i]))
            else:
                print(str(parent[i])+" "+ str(i) +" "+str(weight[i]))
        
li=[int(ele) for ele in input().strip().split()]
n=int(li[0])
E=int(li[1])
g=graph(n)
for i in range(E):
    arr=input().strip().split()
    fv=int(arr[0])
    sv=int(arr[1])
    pv=int(arr[2])
    g.addedge(fv,sv,pv)
g.prims()

