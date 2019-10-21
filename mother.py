from collections import defaultdict

class Graph:

   def __init__(self,V):
      self.vertex=V
      self.graph=defaultdict(list)

   def add_edge(self,u,v):
      self.graph[u].append(v)

   def DFS_util(self,visited,u):
       visited[u]=True
       for i in self.graph[u]:
         if not visited[i]:
            self.DFS_util(visited,i)

   def Mother_vertex(self):
      visited=[False]*self.vertex
      v=0
      for i in range(self.vertex):
         if not visited[i]:
            self.DFS_util(visited,i)
            v=i
      visited=[False]*self.vertex
      self.DFS_util(visited,v)
      if False not in visited:
         print(f"{v} is the mother vertex")
      else:
         print("No mother vertex in the graph")

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edge(0,2)
   graph.add_edge(2,0)
   graph.add_edge(2,3)
   graph.add_edge(3,3)
   graph.add_edge(1,2)
   graph.add_edge(0,1)
   graph.Mother_vertex()

      
            