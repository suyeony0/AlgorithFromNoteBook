N= int(input())

arr=[]
result=[]
for i in range(N):
  temp=input()
  arr.append(temp)
  result.append(temp)
  
for i in range(N): #str�� ��ǲ���� ���� int�� ����ȯ
  arr[i]=arr[i].split(' ')
  arr[i]=list(map(int,arr[i]))
  result[i]=result[i].split(' ')
  result[i]=list(map(int,result[i]))
  
   
for level in range(1,N):
  for i in range(level+1):
    if i==0: #�ش� ������ �� �� ����� ���
      result[level][i]=result[level-1][i]+arr[level][i]
    elif i==level: #�ش� ������ �� �� ����� ���
      result[level][i]=result[level-1][i-1]+arr[level][i]
    else : #�ش� ������ �߰� ����� ���
      result[level][i]=max(result[level-1][i-1],result[level-1][i])+arr[level][i]

print(max(result[N-1]))