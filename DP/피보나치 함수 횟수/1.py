
fiboZero=[1,0,1,1]
fiboOne=[0,1,1,2]

for i in range(4,41):
 
  fiboZero.append(fiboZero[i-1]+fiboZero[i-2])
  fiboOne.append(fiboOne[i-1]+fiboOne[i-2])
  
N=int(input())

arr=[0]*N

for i in range(N):
  arr[i]=int(input())

for i in arr:
  print(str(fiboZero[i])+' '+str(fiboOne[i]))