#���� �������κ��� BFS�� ����� ť
class Queue:
 
  def __init__(self,N):
    self.N=N
    self.top=0
    self.rear=0
    self.queue=[0 for i in range(N)]
    
  def insert(self,value):
    if (self.rear==self.N-1 and self.top==0) or (self.rear==self.top-1):
      #print("Queue is full")
      return
    
    self.queue[self.rear]=value
    self.rear+=1
    if self.rear>=self.N:
      self.rear=0
    
    
  def delete(self):
    if self.top==self.rear:
      #print("Queue is empty")
      return
    
    temp=self.queue[self.top]
    self.top+=1
    if self.top>=self.N:
      self.top=0
    
    return temp
    

#���� �������κ��� DFS�� ����� ����
class Stack:
  
  def __init__(self,N):
    self.top=0
    self.stack=[0 for i in range(N)]
    self.N=N
    
  def push(self,value):
    if self.top==self.N-1:
      #print("Stack is full")
      return
    self.stack[self.top]=value
    
    self.top+=1
    
   
    
  def pop(self):
    if self.top==0:
      #print("Stack is empty")
      return
    self.top-=1
    temp = self.stack[self.top]
    self.stack[self.top]=0   
    return temp
  
  def currentTop(self):
    if top<=0:
      #print("Stack is empty")
      return
   
    return self.stack[self.top-1]


N= input()
N=N.split(' ')

N=list(map(int,N))

graph=[[0 for i in range(N[0]+1)]for i in range(N[0]+1)]
start=N[2]

#�Է¿� ���ؼ� �׷����� ������ ����
for i in range(N[1]):
  temp=input()
  temp=temp.split(' ')
  temp=list(map(int,temp)) # ��ǲ�� int�� ����ȯ
  graph[temp[0]][temp[1]]=1
  graph[temp[1]][temp[0]]=1

# BFS�� DFS Ž�� ��� ������ �迭
BFS=[0 for i in range(N[0])]
BFS[0]=start

DFS=[0 for i in range(N[0])]
DFS[0]=start

top=1

# �湮�Ǿ����� Ȯ���ϱ����� count�迭
count=[0 for i in range(N[0]+1)]
count[start]=1

#Queue �ʱ�ȭ
queue=Queue(N[0]+1)
queue.insert(start)

#BFSŽ��
for i in queue.queue:
  queue.delete()
  if i==0:
    continue
  
  for j in range(1,N[0]+1):
    if graph[i][j]==1 and count[j]==0:
      BFS[top]=j # �ش� ���� �湮
      count[j]=1 #�湮�ߴٴ� ǥ��
      top+=1
      queue.insert(j)
     

  
#count�迭 �ٽ� �ʱ�ȭ
count=[0 for i in range(N[0]+1)]
count[start]=1

#Stack �ʱ�ȭ
stack=Stack(N[0]+1)

stack.push(start)
top=1


#DFSŽ��
while stack.currentTop() !=0:
  current=stack.currentTop()
  
  for i in range(1,N[0]+2):
    if i == N[0]+1:
      stack.pop()
      break
    
    elif graph[current][i]==1 and count[i]==0:
      stack.push(i)
     
      count[i]=1
      DFS[top]=i
      top+=1
      break

# DFS BFS ������ ����ϴ� ����
for i in range(len(DFS)):
  if DFS[i]==0:
    break
  print(DFS[i],end='')
  if i+1==len(DFS):
    break
  print(' ',end='')
  
print()
for i in range(len(BFS)):
  if BFS[i]==0:
    break
  print(BFS[i],end='')
  if i+1==len(BFS):
    break
  print(' ',end='')
        


    