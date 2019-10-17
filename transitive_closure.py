from collections import defaultdict

class Graph:

   def __init__(self,V):
       self.graph=defaultdict(list)
       self.vertex=V

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def DFS_util(self,matrix,u,v):
       matrix[u][v]=1
       for i in self.graph[v]:
          if matrix[u][i]==False:
             self.DFS_util(matrix,u,i)

   def transitive_closure(self):
       matrix=[[0 for i in range(self.vertex)] for j in range(self.vertex)]
       for i in range(self.vertex):
           self.DFS_util(matrix,i,i)
       print(matrix)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.transitive_closure()

          
          