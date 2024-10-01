# 거짓말
# Gold 4, disjoint set

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m = map(int,input().split())
know = tuple(map(int,input().split()))
arr = [tuple(map(int,input().split())) for _ in range(m)]

root = list(range(n+1))
for i in range(m):
    for j in range(1,arr[i][0]):
        a,b = find(arr[i][j]),find(arr[i][j+1])
        root[b] = a

result = [False]*(n+1)
for a in know[1:]:
    result[find(a)] = True

count = 0
for i in range(m):
    if result[find(arr[i][1])] == False: count += 1
print(count)
