# gahui and sousenkyo 7
# Gold 3, constructive

n,c,k = map(int,input().split())
if k == 0:
    for i in range(c-1):
        print(*list(range(1,n+1)))
    print(*list(range(10**6,10**6-n,-1)))
else:
    for _ in range(c-1):
        print(*list(range(1,n+1)))
    prev = 0
    for a in sorted(map(int,input().split())):
        print(*list(range(a,prev,-1)),end=' ')
        prev = a
    for i in range(n-prev):
        print(10**6-i,end=' ')