#시작 정점으로부터 BFS를 사용할 큐
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
    

#시작 정점으로부터 DFS를 사용할 스택
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

#입력에 대해서 그래프의 정점들 연결
for i in range(N[1]):
  temp=input()
  temp=temp.split(' ')
  temp=list(map(int,temp)) # 인풋을 int로 형변환
  graph[temp[0]][temp[1]]=1
  graph[temp[1]][temp[0]]=1

# BFS와 DFS 탐색 결과 저장할 배열
BFS=[0 for i in range(N[0])]
BFS[0]=start

DFS=[0 for i in range(N[0])]
DFS[0]=start

top=1

# 방문되었는지 확인하기위한 count배열
count=[0 for i in range(N[0]+1)]
count[start]=1

#Queue 초기화
queue=Queue(N[0]+1)
queue.insert(start)

#BFS탐색
for i in queue.queue:
  queue.delete()
  if i==0:
    continue
  
  for j in range(1,N[0]+1):
    if graph[i][j]==1 and count[j]==0:
      BFS[top]=j # 해당 정점 방문
      count[j]=1 #방문했다는 표시
      top+=1
      queue.insert(j)
     

  
#count배열 다시 초기화
count=[0 for i in range(N[0]+1)]
count[start]=1

#Stack 초기화
stack=Stack(N[0]+1)

stack.push(start)
top=1


#DFS탐색
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

# DFS BFS 순으로 출력하는 구문
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
        


    