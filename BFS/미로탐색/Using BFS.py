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
    

def find(XYcount):
  
  global x,y
  global result
  global queue
  global visit
  
 
  N=XYcount[0]
  M=XYcount[1]
  count=XYcount[2]
  count+=1

  #도착 쉘
  if N==x and M==y:
    result=count
    
    return count
  
  #오른쪽
  if maze[N][M+1]==1 and visit[N][M+1]==0:
   
    visit[N][M+1]=1
    queue.insert((N,M+1,count))
    
  #아래
  if maze[N+1][M]==1 and visit[N+1][M]==0:
   
    visit[N+1][M]=1
    queue.insert((N+1,M,count))
    
  #위쪽
  if maze[N-1][M]==1 and visit[N-1][M]==0:
    
    visit[N-1][M]=1
    queue.insert((N-1,M,count))
    
  #왼쪽
  if maze[N][M-1]==1 and visit[N][M-1]==0:
   
    visit[N][M-1]=1
    queue.insert((N,M-1,count))
    
    
  return 999
  
  
    
temp = input()
temp=temp.split(' ')
N=int(temp[0])
M=int(temp[1])
x=N
y=M

result=-1
top=0
maze=[[0 for i in range(M+2)]for i in range(N+2)]
visit=[[0 for i in range(M+2)]for i in range(N+2)]
visit[1][1]=1

queue=Queue(10001)
queue.insert((1,1,0))

#감싼 미로 가운데에 인풋 집어넣기  
for i in range(1,N+1):
  temp=input()
  temp=list(map(int,temp))
  
  for j in range(1,M+1):
    maze[i][j]=temp[j-1]


i=queue.delete()

while i!=None:
  
  find(i)
  if result!=-1:
    print(result)
    break
  
  i=queue.delete()

  

