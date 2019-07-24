N=int(input())

if N == 1 : print(1)
elif N==2 : print(2)
  
result=[1,2]

for i in range(2,N):
  result.append(result[i-1]+result[i-2])

print(result[-1])
