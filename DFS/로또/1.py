def dfs(k,current,start,depth):
    global arr

    if depth==6:
        current=list(map(str,current))
        print(' '.join(current))
        return

    for i in range(start,len(arr[k])):
        current[depth]=arr[k][i]

        dfs(k,current,i+1,depth+1)




arr=[]

while True:
    temp=input()
    if temp=='0':
        break
    temp=temp.split(' ')
    temp=list(map(int,temp))
    arr.append(temp)


for k in range(len(arr)):
    current=[0 for i in range(6)]
    dfs(k,current,1,0)
    print()
