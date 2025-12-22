# 카드 섞기
# Gold 5, implementation, bruteforcing, simulation

N = int(input())
arr = list(map(int,input().split()))

for k1 in range(10):
    if 2**k1 > N: break
    temp1 = list(range(1,N+1))
    temp1 = temp1[-2**k1:]+temp1[:-2**k1]
    for i in range(k1-1,-1,-1):
        temp1[:2**i],temp1[2**i:2**(i+1)] = temp1[2**i:2**(i+1)],temp1[:2**i]
    for k2 in range(10):
        if 2**k2 > N: break
        temp2 = temp1[:]
        temp2 = temp2[-2**k2:]+temp2[:-2**k2]
        for i in range(k2-1,-1,-1):
            temp2[:2**i],temp2[2**i:2**(i+1)] = temp2[2**i:2**(i+1)],temp2[:2**i]
        if temp2 == arr:
            exit(print(k1,k2))