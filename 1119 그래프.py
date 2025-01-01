# 그래프
# Gold 2, disjoint set

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N = int(input())
arr = [input() for _ in range(N)]

if N == 1: exit(print(0))

root = list(range(N))
c = 0
for i in range(N):
    if 'Y' not in arr[i]:
        exit(print(-1))
    for j in range(i+1,N):
        if arr[i][j] == 'Y':
            a,b = find(i),find(j)
            root[b] = a
            c += 1

answer = -1
for i in range(N):
    if find(i) == i:
        answer += 1
print(answer if c >= N-1 or answer == 0 else -1)