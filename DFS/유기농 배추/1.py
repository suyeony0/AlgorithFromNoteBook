import queue


def find(k):

  global count
  global field
  global stack

  while stack.qsize()!=0:

    orientation=stack.get()
    x=orientation[0]
    y=orientation[1]

    #위쪽
    if field[k][x-1][y]==1:
      field[k][x-1][y]=2
      stack.put((x-1,y))
      count+=1

    #아래쪽
    if field[k][x+1][y]==1:
      field[k][x+1][y]=2
      stack.put((x+1,y))
      count+=1

    #왼쪽
    if field[k][x][y-1]==1:
      field[k][x][y-1]=2
      stack.put((x,y-1))
      count+=1

    #오른쪽
    if field[k][x][y+1]==1:
      field[k][x][y+1]=2
      stack.put((x,y+1))
      count+=1



stack=queue.LifoQueue()

numberOfTestCase = int(input())
result=[0 for i in range(numberOfTestCase)]
field=[0 for i in range(numberOfTestCase)]
N=[0 for i in range(numberOfTestCase)]
M=[0 for i in range(numberOfTestCase)]
for i in range(numberOfTestCase):

  temp= input()
  temp=temp.split(' ')
  M[i]=int(temp[0])
  N[i]=int(temp[1])
  cabbage=int(temp[2])
  count=0

  field[i]=[[0 for j in range(M[i]+2)]for j in range(N[i]+2)]

  for j in range(cabbage):
    temp2=input()
    temp2=temp2.split(' ')
    field[i][int(temp2[1])+1][int(temp2[0])+1]=1



for k in range(numberOfTestCase):
  for i in range(1,N[k]+1):
    for j in range(1,M[k]+1):

      if field[k][i][j]==1:
        result[k]+=1
        count+=1
        field[k][i][j]=2
        stack.put((i,j))
        find(k)

for i in range(numberOfTestCase):
  print(result[i])
