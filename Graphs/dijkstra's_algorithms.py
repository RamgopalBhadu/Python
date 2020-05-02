#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist):
        for node in range(self.V): 
            print (node, dist[node] )
            
    def addedge(self,v1,v2,wt):
        self.graph[v1][v2]=wt
        self.graph[v2][v1]=wt
    
    def minDistance(self, dist, sptSet): 

        min = sys.maxsize 

        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 

    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 

            u = self.minDistance(dist, sptSet) 

            sptSet[u] = True
 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist)

li=[int(ele) for ele in input().strip().split()]
n=int(li[0])
E=int(li[1])
g=Graph(n)
for i in range(E):
    arr=input().strip().split()
    fv=int(arr[0])
    sv=int(arr[1])
    pv=int(arr[2])
    g.addedge(fv,sv,pv)
g.dijkstra(0)

