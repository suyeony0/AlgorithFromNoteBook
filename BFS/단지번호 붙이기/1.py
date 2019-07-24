import queue

def find(position):
  global count
  global Houses
  current=0
  
  while q.qsize()!=0:
    
    temp=q.get()
    X=temp[0]
    Y=temp[1]
   
    #위쪽
    if Houses[X-1][Y]==1:
      current+=1
      count+=1
      q.put((X-1,Y))
      Houses[X-1][Y]=position
    #아래쪽
    if Houses[X+1][Y]==1:
      current+=1
      count+=1
      q.put((X+1,Y))
      Houses[X+1][Y]=position
    #왼쪽
    if Houses[X][Y-1]==1:
      current+=1
      count+=1
      q.put((X,Y-1))
      Houses[X][Y-1]=position
    #오른쪽
    if Houses[X][Y+1]==1:
      current+=1
      count+=1
      q.put((X,Y+1))
      Houses[X][Y+1]=position

  
  return current
  

q=queue.Queue()
Ones=0
count=0
position=5
N=int(input())
Houses=[[0]for i in range(N+2)]
result=[N*N+1 for i in range(N*N)]
top=0
for i in range(1,N+1):
  temp=input()
  for j in temp:
    if 1== int(j):
      Ones+=1
  Houses[i]=Houses[i]+list(map(int,temp))+Houses[i]
  
Houses[0]=[0 for i in range(N+2)]
Houses[N+1]=[0 for i in range(N+2)]

numberOfStreet=0

for i in range(1,N+1):
  for j in range(1,N+1):
    if Houses[i][j]==1:
      numberOfStreet+=1
      count+=1
      q.put((i,j))
      Houses[i][j]=position
      position+=1
      result[top]=find(position)+1
      
      top+=1
  



result.sort()
print(numberOfStreet)
for i in range(numberOfStreet):
  print(result[i])
