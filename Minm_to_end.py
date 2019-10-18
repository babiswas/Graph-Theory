class Cell:
   def __init__(self,pos,dist):
      self.pos=pos
      self.dist=dist

def isinside(x,N):
    if x<0 or x>=N:
      return False
    return True


def BFS(l,x):
   dx=[-1,1]
   queue=[]
   visited=[False]*len(l)
   queue.append(Cell(x,0))
   visited[x]=True
   while queue:
       m=queue.pop(0)
       if m.pos==(len(l)-1):
          return m.dist
       #print(f"{m.pos}")
       index_arr=[i for i,j in enumerate(l) if j==l[m.pos]]
       index_arr.remove(m.pos)
       for i in range(2):
          a=m.pos+dx[i]
          if visited[a]==False and isinside(a,len(l)):
              queue.append(Cell(a,m.dist+1))
       if index_arr:
          for i in index_arr:
              if visited[i]==False:
                  queue.append(Cell(i,m.dist+1))

if __name__=="__main__":
   arr=[0,1,2,3,4,5,6,7,5,4,3,6,0,1,2,3,4,5,7]
   N=len(arr)
   print(BFS(arr,0))


       
          
      
         
   
