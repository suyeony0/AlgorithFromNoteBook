class Queue:
 
  def __init__(self,N):
    self.N=N
    self.top=0
    self.rear=0
    self.queue=[0 for i in range(N)]
    
  def insert(self,value):
    if (self.rear==self.N-1 and self.top==0) or (self.rear==self.top-1):
      
      return
    
    self.queue[self.rear]=value
    self.rear+=1
    if self.rear>=self.N:
      self.rear=0
    
    
  def delete(self):
    if self.top==self.rear:
      
      return
    
    temp=self.queue[self.top]
    self.top+=1
    if self.top>=self.N:
      self.top=0
    
    return temp
 
class node:
  
  def __init__(self,value):
    self.value=value
    self.left=None
    self.right=None
    self.double=None
    self.visit=False
    self.searched=False
    self.count=0
 
    
def find(temp,count):
  
  global queue
  global Brother
  global head
  
 
  if temp==Brother:
    
    return head[temp].count
  
  if head[temp].left!=None:
    if head[temp].left.visit==False:
      if head[temp].left.searched==False:
        head[temp].left.searched=True
        head[temp].left.count=head[temp].count+1
      queue.insert(head[temp].left)
    
  if head[temp].right!=None :
    if head[temp].right.visit==False:
      if head[temp].right.searched==False:
        head[temp].right.searched=True
        head[temp].right.count=head[temp].count+1
      
      queue.insert(head[temp].right)
  if head[temp].double!=None and head[temp].double.visit==False :
    if head[temp].double.searched==False:
        head[temp].double.searched=True
        head[temp].double.count=head[temp].count+1
    
    queue.insert(head[temp].double)

  return -1
  

temp = input()
temp=temp.split(' ')
Subin=int(temp[0])
Brother=int(temp[1])
maximum=100000
count=0
result=-1
if Subin==Brother:
  print(0)



else:

  head=[node(0)for i in range(maximum*2+2)]

  #그래프 초기화
  for i in range(1,maximum*2+2):
    head[i].value=i
  for i in range(1,maximum*2+1):
    head[i].left=head[i-1]
    head[i].right=head[i+1]
    if i<=100000 :
      head[i].double=head[i*2]
 
  
  #수빈이 좌표가 0일경우
  if Subin==0:
    count+=1
    Subin=1
 
  queue=Queue(maximum+2)
  queue.insert(head[Subin])
  i=queue.delete()
  i.count=count
  i.searched=True
  while i!=None:
    i.visit=True
   
  
    result=find(i.value,i.count)
    if result!=-1:
      print(result)
      break
    i=queue.delete()
  
   
  
  