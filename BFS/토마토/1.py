#모든 익은 토마토에 대하여 BFS를 하고
#모든 토마토가 익으면 끝
class Queue:
  
  
  def __init__(self,N):
    self.N=N
    self.top=0
    self.rear=0
    self.queue=[None for i in range(N)]
    
  def insert(self,value):
    if (self.rear==self.N-1 and self.top==0) or (self.rear==self.top-1):
      
      return
    
    self.queue[self.rear]=value
    self.rear+=1
    if self.rear>=self.N:
      self.rear=0
    
  def showTop(self):
    return self.top
  
  def showRear(self):
    return self.rear
  
  def delete(self):
    if self.top==self.rear:
      
      return
    
    temp=self.queue[self.top]
    self.top+=1
    if self.top>=self.N:
      self.top=0
    
    return temp
 




def find():
  #number는 몇번째 queue에서 실행 중인지 확인하기위한 변수
  #queue에는 좌표 튜플이 등록되어있음
  global box
  global N,M
  global queue
  global current
  global count
  nowRear=queue.showRear() 
 
  while nowRear!=queue.showTop():
    
    i=queue.delete()
    X=i[0]
    Y=i[1]
    #오른쪽
    if box[X][Y+1]==0 :
      
      current+=1
      
      box[X][Y+1]=1 #익음
      queue.insert((X,Y+1)) #다른 queue에 순서대로 입력
      
    #아래쪽
    if box[X+1][Y]==0:
      
      current+=1
      
      box[X+1][Y]=1 #익음
      queue.insert((X+1,Y)) #다른 queue에 순서대로 입력
    #위쪽
    if box[X-1][Y]==0:
      
      current+=1
     
      box[X-1][Y]=1 #익음
      queue.insert((X-1,Y)) #다른 queue에 순서대로 입력
      
    #왼쪽  
    if box[X][Y-1]==0 :
      
      current+=1
      
      box[X][Y-1]=1 #익음
      queue.insert((X,Y-1)) #다른 queue에 순서대로 입력
     
    
  

temp=input()
temp=temp.split(' ')
N=int(temp[1])
M=int(temp[0])

maximum=N*M
minusOne=0
current=0
#박스 주변을 막기위해 더 큰 박스 선언
box=[[-1] for i in range(N*2)]

#Queue초기화
#번갈아써야 하므로 2개 선언
#arr=[N*M for i in range(2)]
queue=Queue(N*M)
#이거 queue=[Queue(N*M)] *2 하면 얕은 복사 즉, 주소값이 동일하게 할당됨
#신기하네...
impossible=0
#박스 초기화
box[0]=[-1 for i in range(M*2)]
box[N+1]=[-1 for i in range(M*2)]

for i in range(1,N+1):
  temp=input()
  temp=temp.split(' ')
  box[i]=box[i]+(list(map(int,temp)))+box[i]
  
  for j in range(1,M+1):
    if int(temp[j-1])==1:
      current+=1
      queue.insert((i,j))
    elif int(temp[j-1])==-1:
      minusOne+=1

             
count=0
maximum=maximum-minusOne

number=0
a=0

while current!=maximum:
  impossible=current # impossible인지 체크하기위함
  count+=1
  find()
  
  
  if impossible==current:
    impossible=1
    break
 
  
    
if impossible==1:
  print(-1)
else:
  print(count)
