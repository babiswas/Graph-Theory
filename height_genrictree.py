def array_tree(arr):
   adj=[[] for i in range(len(arr))]
   for i in range(len(arr)):
      if arr[i]==-1:
         pass
      else:
         adj[arr[i]].append(i)
   return adj

def BFS(adj,arr):
   visited=[False]*len(adj)
   queue=[]
   count=0
   queue.append(arr.index(-1))
   visited[arr[arr.index(-1)]]=True
   while queue:
      q_length=len(queue)
      while q_length:
          m=queue.pop(0)
          for i in adj[m]:
             if not visited[i]:
                queue.append(i)
                visited[i]=True
          q_length=q_length-1
      count=count+1
   return count

def calculate_height(arr):
   adj=array_tree(arr)
   print(adj)
   count=BFS(adj,arr)
   print(f"The height of the tree is {count}")
    

if __name__=="__main__":
   arr=[-1,0,0,0,3,1,1,2]
   calculate_height(arr)
   
          