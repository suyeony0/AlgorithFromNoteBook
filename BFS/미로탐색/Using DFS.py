import copy
#함수로 스택을 대신함
def find(N,M,count,visit):
  #여기에 함수 만들어주면됨
  count+=1
  global maze
  global n,m
  global top
  global result
  
  #visit을 그대로쓰면 call by reference라서 계속 갱신되어
  #현재 스택이 유지해야하는 visit배열을 유지하지 못함
  #그래서 call by value를 강제로 실행해줌
  #그 visit배열이 temp
  
  #근데 이렇게 call by value하면 시간초과가 뜸 
  #진퇴양난이다...
  #그래서 깊은복사를 시전했다.
  #하지만 여전히 시간초과..

  temp=copy.deepcopy(visit)
 
  
 
  
  #도착 쉘
  if N==n and M==m :
    result[top]=count
    top+=1
    return count  
  
  #오른쪽
  if maze[N][M+1]==1 and temp[N][M+1]==0:
    temp[N][M+1]=1
    find(N,M+1,count,temp)
    
   
  #아래
  if maze[N+1][M]==1 and temp[N+1][M]==0:
    temp[N+1][M]=1
    find(N+1,M,count,temp)
    
  #위쪽
  if maze[N-1][M]==1 and temp[N-1][M]==0:
    temp[N-1][M]=1
    find(N-1,M,count,temp)
   
  #왼쪽
  if maze[N][M-1]==1 and temp[N][M-1]==0:
    temp[N][M-1]=1
    find(N,M-1,count,temp)
    
  return 999
  
temp=input()
temp=temp.split(' ')
N=int(temp[0])
M=int(temp[1])
n=N
m=M
top=0
result=[999 for i in range(M*N)]
maze=[[0 for i in range(M+2)]for i in range(N+2)]
visit=[[0 for i in range(M+2)]for i in range(N+2)]
visit[1][1]=1


#감싼 미로 가운데에 인풋 집어넣기  
for i in range(1,N+1):
  temp=input()
  temp=list(map(int,temp))
  
  for j in range(1,M+1):
    maze[i][j]=temp[j-1]

find(1,1,0,visit)
print(min(result))
