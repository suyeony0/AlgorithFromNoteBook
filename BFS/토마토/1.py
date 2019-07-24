#��� ���� �丶�信 ���Ͽ� BFS�� �ϰ�
#��� �丶�䰡 ������ ��
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
  #number�� ���° queue���� ���� ������ Ȯ���ϱ����� ����
  #queue���� ��ǥ Ʃ���� ��ϵǾ�����
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
    #������
    if box[X][Y+1]==0 :
      
      current+=1
      
      box[X][Y+1]=1 #����
      queue.insert((X,Y+1)) #�ٸ� queue�� ������� �Է�
      
    #�Ʒ���
    if box[X+1][Y]==0:
      
      current+=1
      
      box[X+1][Y]=1 #����
      queue.insert((X+1,Y)) #�ٸ� queue�� ������� �Է�
    #����
    if box[X-1][Y]==0:
      
      current+=1
     
      box[X-1][Y]=1 #����
      queue.insert((X-1,Y)) #�ٸ� queue�� ������� �Է�
      
    #����  
    if box[X][Y-1]==0 :
      
      current+=1
      
      box[X][Y-1]=1 #����
      queue.insert((X,Y-1)) #�ٸ� queue�� ������� �Է�
     
    
  

temp=input()
temp=temp.split(' ')
N=int(temp[1])
M=int(temp[0])

maximum=N*M
minusOne=0
current=0
#�ڽ� �ֺ��� �������� �� ū �ڽ� ����
box=[[-1] for i in range(N*2)]

#Queue�ʱ�ȭ
#�����ƽ�� �ϹǷ� 2�� ����
#arr=[N*M for i in range(2)]
queue=Queue(N*M)
#�̰� queue=[Queue(N*M)] *2 �ϸ� ���� ���� ��, �ּҰ��� �����ϰ� �Ҵ��
#�ű��ϳ�...
impossible=0
#�ڽ� �ʱ�ȭ
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
  impossible=current # impossible���� üũ�ϱ�����
  count+=1
  find()
  
  
  if impossible==current:
    impossible=1
    break
 
  
    
if impossible==1:
  print(-1)
else:
  print(count)
