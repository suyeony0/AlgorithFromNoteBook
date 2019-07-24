

Stairs=int(input())

valueOfStairs=[0]*Stairs
result=[0]*Stairs

for i in range(Stairs):
  valueOfStairs[i]=int(input())

result[0]=valueOfStairs[0]
result[1]=valueOfStairs[1] + valueOfStairs[0]
result[2]=max(valueOfStairs[0]+valueOfStairs[2],valueOfStairs[1]+valueOfStairs[2])
  
for i in range(3,Stairs):
  result[i]=max(result[i-3]+valueOfStairs[i-1]+valueOfStairs[i],
                result[i-2]+valueOfStairs[i])

print(result[-1])

