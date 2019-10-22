from collections import defaultdict

class Graph:
   def __init__(self,V):
      self.vertex=V
      self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def DFS(self,u):
     visited=[False]*self.vertex
     self.DFS_util(visited,u)

   def DFS_util(self,visited,u):
       visited[u]=True
       print(u)
       for i in self.graph[u]:
          if not visited[i]:
             self.DFS_util(visited,i)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.DFS(2)

