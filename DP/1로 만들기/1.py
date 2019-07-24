def MakeItOne(arr,N):
  arr[1]=0
  for i in range(2,N+1):
    arr[i]=arr[i-1]+1
    if i%2==0 : arr[i]=min(arr[i],arr[int(i/2)]+1)
    if i%3==0 : arr[i]=min(arr[i],arr[int(i/3)]+1)
  return arr


N=int(input())

if (N==3 or N==2) :
  print(1)
elif N==1 : print(0)

else :
  arr = [0]*(N+1)
  arr=MakeItOne(arr,N)
  print(arr[-1])