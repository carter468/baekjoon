# 스왑 스왑
# Gold 2, parity, fenwick tree

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i):
    while i <= N:
        tree[i] += 1
        i += (i&-i)

N = int(input())
A = tuple(map(int,input().split()))

tree = [0]*(N+1)
count = 0
for i in range(N):
    count += i-prefix_sum(A[i])
    update(A[i])

print('No' if count%2 else 'Yes')