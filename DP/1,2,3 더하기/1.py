numberOfTestCase = int(input())

arr = [0]*numberOfTestCase
for i in range(numberOfTestCase):
  arr[i]=int(input())

result = [0,1,2,4]

for i in range(4,12):
  result.append(result[i-1]+result[i-2]+result[i-3])

for i in arr:
  print(result[i])
