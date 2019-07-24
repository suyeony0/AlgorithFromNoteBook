N= int(input())

result=[0,1]

for i in range(2,N+1):
  result.append(result[i-1]+result[i-2])
  
print(result[-1])
  