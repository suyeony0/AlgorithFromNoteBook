def fibo(N):
    if N==1 : return 1
    elif N==2 : return 2
    return fibo(N-1)+fibo(N-2)

    
N=int(input())
print(fibo(N)%15746)
    