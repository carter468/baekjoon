# 사전 순 최대 공통 부분 수열
# Gold 4, greedy

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

arr = []
for i in range(n):
    arr.append((A[i],i))
arr.sort(key=lambda x:-x[0])

result = []
idx_a = -1
idx_b = -1
for a,idx in arr:
    if idx < idx_a: continue
    for i in range(idx_b+1,m):
        if a == B[i]:
            result.append(a)
            idx_a = idx
            idx_b = i
            break

print(len(result))
if result: print(*result)