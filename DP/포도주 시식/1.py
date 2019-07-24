#난 이게 왜 안풀리는지 이해가 안감
#아무리 생각해도 맞거든? 근데 파이썬으로는 안되고 C++로는 풀림
#ㄹㅇ 이거는 백준 홈페이지 문제다...

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
  

