# 5교시: 과학
# Platinum 5, MITM

N = int(input())
W = tuple(map(int,input().split()))
P = tuple(map(int,input().split()))
arr = sorted([(P[i],W[i]) for i in range(N)])

count1 = dict()
count2 = dict()
n = N//2
m = N-n
mid = arr[n-1][0]
for i in range(1,1<<n):
    x = 0
    pos = set()
    for j in range(n):
        if i>>j&1:
            p,w = arr[j]
            if p in pos:
                break
            x += (5000-p)*w
            pos.add(p)
    else:
        if mid in pos:
            count1[x] = count1.get(x,0)+1
        else:
            count2[x] = count2.get(x,0)+1

result = count1.get(0,0)+count2.get(0,0)
count2[0] = count2.get(0,0)+1
for i in range(1,1<<m):
    x = 0
    pos = set()
    for j in range(m):
        if i>>j&1:
            p,w = arr[j+n]
            if p in pos:
                break
            x -= (5000-p)*w
            pos.add(p)
    else:
        result += count2.get(x,0)
        if mid not in pos:
            result += count1.get(x,0)
print(result)