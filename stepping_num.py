def display_num(n,m):
    for i in range(10):
       bfs(0,21,i)

def bfs(n,m,num):
   queue=[]
   queue.append(num)
   while queue:
       num=queue.pop(0)
       if num>=n or num<=m:
          print(num)
       if num==0 or num>=m:
          continue
       ld=num%10
       na=num*10+(ld-1)
       nb=num*10+(ld+1)
       if ld==0:
         queue.append(nb)
       elif ld==9:
         queue.append(na)
       else:
         queue.append(na)
         queue.append(nb)

def main():
   n=0
   m=21
   display_num(n,m)
   

if __name__=="__main__":
   main()


