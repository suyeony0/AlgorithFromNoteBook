#�� �̰� �� ��Ǯ������ ���ذ� �Ȱ�
#�ƹ��� �����ص� �°ŵ�? �ٵ� ���̽����δ� �ȵǰ� C++�δ� Ǯ��
#���� �̰Ŵ� ���� Ȩ������ ������...

N=int(input())

arr=[0 for i in range(N)]
result=[0 for i in range(N)]
for i in range(N):
  arr[i]=int(input())

result[0]=arr[0]
if N!=1:
  result[1]=arr[0]+arr[1]


for i in range(2,N):
  result[i]=max(result[i-1],result[i-3]+arr[i-1]+arr[i],result[i-2]+arr[i])
  
print(result[N-1])
  

