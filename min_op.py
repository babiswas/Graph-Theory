import queue

class Node:
   def __init__(self,val,level):
       self.val=val
       self.level=level

def min_operation(x,y):
    visit=set()
    q=queue.Queue()
    node=Node(x,0)
    q.put(node)
    while not q.empty():
        m=q.get()
        if m.val==y:
           return m.level
        visit.add(m.val)
        if (m.val*2==y) or(m.val-1==y):
              return m.val+1
        if (m.val*2 not in visit):
           node.val=m.val*2
           node.level=m.level+1
           q.put(node)
        if m.val-1>=0 and m.val-1 not in visit:
           node.val=m.val-1
           node.level=m.level+1
           q.put(node)

if __name__=="__main__":
   x=4
   y=7
   print(min_operation(x,y))
