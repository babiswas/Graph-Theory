from collections import defaultdict
class Graph:
   def __init__(self,V):
      self.vertex=V
      self.graph=defaultdict(list)
   def add_edge(self,u,v):
      self.graph[u].append(v)
      self.graph[v].append(u)
   def K_core_decompose(self,k):
      value=True
      while value:
         queue=[]
         for i in self.graph:
            if len(self.graph[i])<k:
               queue.append(i)
         for i in queue:
            del self.graph[i]
         if queue:
            for i in self.graph:
               for j in self.graph[i]:
                  if j in queue:
                     self.graph[i].remove(j)
         else:
            break

         queue[:]=[]
      for i in self.graph:
         print(f"{i}--->{self.graph[i]}")

if __name__=="__main__":
   k = 3;
   g1 = Graph (9)
   g1.add_edge(0,1)
   g1.add_edge(0,2)
   g1.add_edge(1,2)
   g1.add_edge(1,5)
   g1.add_edge(2,3)
   g1.add_edge(2,4)
   g1.add_edge(2,5)
   g1.add_edge(2,6)
   g1.add_edge(3,4)
   g1.add_edge(3,6)
   g1.add_edge(3,7)
   g1.add_edge(4,6)
   g1.add_edge(4,7)
   g1.add_edge(5,6)
   g1.add_edge(5,8)
   g1.add_edge(6,7)
   g1.add_edge(6,8)
   g1.K_core_decompose(3)