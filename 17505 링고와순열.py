# 링고와 순열
# Gold 5, greedy

n,k = map(int,input().split())

if k == 0: 
    print(*range(1,n+1))
    exit() 
while k > 0: 
    if n-1 < k: 
        print(n,end=' ') 
        k -= n-1 
        n -= 1 
    else: 
        for i in range(n-1-k): 
            print(i+1,end=' ') 
            print(n,end=' ') 
        for i in range(n-k,n): 
            print(i,end=' ') 
        break
