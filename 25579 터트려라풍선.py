# 터트려라 풍선
# Gold 2, disjoint set

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N = int(input())
B = tuple(map(int,input().split()))
P = tuple(map(int,input().split()))

result = 0
root = [0]*(N+2)
size = [0]*(N+1)
point = [0]*(N+1)
score = 0

for i in P[:0:-1]:
    point[i] = B[i-1]
    size[i] = 1
    root[i] = i
    score += B[i-1]
    for j in (i-1,i+1):
        if j := find(j):
            i = find(i)
            if i > j: i,j = j,i
            score -= size[i]*point[i]+size[j]*point[j]
            size[i] += size[j]
            point[i] += point[j]
            root[j] = i
            score += size[i]*point[i]
    result = max(result,score)
print(result)