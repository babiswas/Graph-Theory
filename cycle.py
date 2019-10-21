from collections import defaultdict
#Detect cycle in a directed graph.

class Graph:

   def __init__(self,V):
      self.graph=defaultdict(list)
      self.vertex=V

   def add_edge(self,u,v):
      self.graph[u].append(v)

   def isCyclic_util(self,visited,recstack,u):
       visited[u]=True
       recstack[u]=True
       for i in self.graph[u]:
         if not visited[i]:
           if self.isCyclic_util(visited,recstack,i):
              return True
         elif i in recstack:
              return True
       recstack[u]=False
       return False

   def Cycle_detect(self):
       visited=[False]*self.vertex
       recstack=[False]*self.vertex
       for i in range(self.vertex):
           if not visited[i]:
             if self.isCyclic_util(visited,recstack,i):
                return True
       return False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edge(1,2)
   graph.add_edge(0,2)
   graph.add_edge(2,0)
   graph.add_edge(3,3)
   graph.add_edge(2,3)
   graph.add_edge(0,1)
   print(graph.Cycle_detect())
   

   