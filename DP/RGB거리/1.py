
N=int(input())

arr=[[0 for i in range(3)] for i in range(N+1)]

for i in range(1,N+1):
  temp=input()
  arr[i]=temp.split(' ')

for i in range(N+1): #�Է°� int�� �ٲ��ְ�
  arr[i][0]=int(arr[i][0])
  arr[i][1]=int(arr[i][1])
  arr[i][2]=int(arr[i][2])

result=[[0 for i in range(3)] for i in range(N+1)]

for i in range(1,N+1): 
  # ���� �ε������� �� ����� �ٸ� ������ �� ���� ��� �� ���� ���� ��ü
  result[i][0]=min(result[i-1][1],result[i-1][2])+arr[i][0]
  result[i][1]=min(result[i-1][0],result[i-1][2])+arr[i][1]
  result[i][2]=min(result[i-1][0],result[i-1][1])+arr[i][2]
  
print(min(result[N]))

