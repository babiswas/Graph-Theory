class Cell:
    def __init__(self,x=0,y=0,dist=0):
       self.x=x
       self.y=y
       self.dist=dist

def isinside_block(x,y,N,M):
    if x<0 or x>=N:
       return False
    if y<0 or y>=N:
       return False
    if M[x][y]=='#':
       return False
    return True

def solve_dungeon(kpos,N,M):
   dx=[1,-1,0,0]
   dy=[0,0,1,-1]
   queue=[]
   visited=[[False for i in range(N)]for j in range(N)]
   queue.append(Cell(kpos[0],kpos[1],0))
   visited[kpos[0]][kpos[1]]=True
   while queue:
      m=queue.pop(0)
      print(f"{m.x},{m.y},{m.dist}")
      if M[m.x][m.y]=='E':
        return m.dist
      for i in range(4):
        x=m.x+dx[i]
        y=m.y+dy[i]
        if isinside_block(x,y,N,M):
           if visited[x][y]==False:
                queue.append(Cell(x,y,m.dist+1))
                visited[x][y]=True
   return -1

if __name__=="__main__":
  N=4
  M=[[3,3,1,'#'],[3,'#',3,3],['E',3,'#',3],['#',3,3,3]]
  kpos=[0,2]
  print(solve_dungeon(kpos,N,M))
  
