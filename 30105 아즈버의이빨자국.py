# 아즈버의 이빨 자국
# Gold 5, bruteforcing, hash_set

n = int(input())
arr = tuple(map(int,input().split()))

set_arr = set(arr)
idx = {}
for i in range(n):
    idx[arr[i]] = i

result = []
for i in range(1,n):
    k = arr[i]-arr[0]
    visit = [0]*n
    visit[0],visit[i] = 1,1
    for j in range(1,n-1):
        if arr[j]+k in set_arr:
            visit[j],visit[idx[arr[j]+k]] = 1,1
        elif visit[j] == 0:
            break
    if sum(visit) == n:
        result.append(k)

print(len(result))
if result: print(*result)