# 분배
# Gold 4, 수학

n,k = map(int,input().split())

m = 2**n-1
i = 0
for _ in range(2**k):
    for _ in range(2**(n-k-1)):
        print(i,m-i,end=' ')
        i += 1
    print()