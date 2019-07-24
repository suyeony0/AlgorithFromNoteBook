N= int(input())

arr=[]
result=[]
for i in range(N):
  temp=input()
  arr.append(temp)
  result.append(temp)
  
for i in range(N): #str로 인풋받은 것을 int로 형변환
  arr[i]=arr[i].split(' ')
  arr[i]=list(map(int,arr[i]))
  result[i]=result[i].split(' ')
  result[i]=list(map(int,result[i]))
  
   
for level in range(1,N):
  for i in range(level+1):
    if i==0: #해당 레벨의 맨 앞 노드의 경우
      result[level][i]=result[level-1][i]+arr[level][i]
    elif i==level: #해당 레벨의 맨 뒤 노드의 경우
      result[level][i]=result[level-1][i-1]+arr[level][i]
    else : #해당 레벨의 중간 노드의 경우
      result[level][i]=max(result[level-1][i-1],result[level-1][i])+arr[level][i]

print(max(result[N-1]))