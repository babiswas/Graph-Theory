#Single Source shortest path.
class Graph:
     def __init__(self,V):
         self.graph=[]
         self.vertex=V

     def add_edges(self,u,v,w):
         self.graph.append([u,v,w])

     def print_paths(self,dist):
        for u,v,w in self.graph:
           print(f"(0,{v})----->{dist[v]}")


     def bellman_ford(self,src):
         dist=[float("Inf")]*self.vertex
         dist[src]=0
         self.print_paths(dist)
         for i in range(self.vertex-1):
            for u,v,w in self.graph:
               if dist[u]!=float("Inf") and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w

         print("After bellman ford")
         self.print_paths(dist)
         print("After Bellman ford")
         for i in range(self.vertex):
            print(f"{i}--->{dist[i]}")
         for i in self.graph:
            if dist[u]+w<dist[v]:
                print(f"Edge ({u},{v},{w}) effected by cycle")
          


if __name__=="__main__":
   graph=Graph(5)
   graph.add_edges(0,1,-1)
   graph.add_edges(0,2,4)
   graph.add_edges(1,2,3)
   graph.add_edges(1,3,2)
   graph.add_edges(1,4,2)
   graph.add_edges(3,2,5)
   graph.add_edges(3,1,1)
   graph.add_edges(4,3,-3)
   graph.bellman_ford(0)

         