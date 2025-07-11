# 월향 조각사
# Gold 3, ad hoc

N = int(input())
A = tuple(map(int,input().split()))

arr1 = [0]*N
arr2 = [0]*N
m = 0
for i in range(N):
    if A[i] >= m+1: m += 1
    else: m = min(m,A[i])
    arr1[i] = m
m = 0
for i in range(N-1,-1,-1):
    if A[i] >= m+1: m += 1
    else: m = min(m,A[i])
    arr2[i] = m

result = 0
for i in range(N):
    result += min(arr1[i],arr2[i])
print(result)