import copy
#�Լ��� ������ �����
def find(N,M,count,visit):
  #���⿡ �Լ� ������ָ��
  count+=1
  global maze
  global n,m
  global top
  global result
  
  #visit�� �״�ξ��� call by reference�� ��� ���ŵǾ�
  #���� ������ �����ؾ��ϴ� visit�迭�� �������� ����
  #�׷��� call by value�� ������ ��������
  #�� visit�迭�� temp
  
  #�ٵ� �̷��� call by value�ϸ� �ð��ʰ��� �� 
  #����糭�̴�...
  #�׷��� �������縦 �����ߴ�.
  #������ ������ �ð��ʰ�..

  temp=copy.deepcopy(visit)
 
  
 
  
  #���� ��
  if N==n and M==m :
    result[top]=count
    top+=1
    return count  
  
  #������
  if maze[N][M+1]==1 and temp[N][M+1]==0:
    temp[N][M+1]=1
    find(N,M+1,count,temp)
    
   
  #�Ʒ�
  if maze[N+1][M]==1 and temp[N+1][M]==0:
    temp[N+1][M]=1
    find(N+1,M,count,temp)
    
  #����
  if maze[N-1][M]==1 and temp[N-1][M]==0:
    temp[N-1][M]=1
    find(N-1,M,count,temp)
   
  #����
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


#���� �̷� ����� ��ǲ ����ֱ�  
for i in range(1,N+1):
  temp=input()
  temp=list(map(int,temp))
  
  for j in range(1,M+1):
    maze[i][j]=temp[j-1]

find(1,1,0,visit)
print(min(result))
