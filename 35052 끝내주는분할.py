# 끝내주는 분할
# Platinum 5, fenwick tree, ad hoc

def prefix_sum(tree,v,i):
    result = 0
    while i > 0:
        if v[i] != count:
            tree[i] = 0
            v[i] = count
        result += tree[i]
        i -= (i&-i)
    return result

def update(tree,v,i):
    while i <= N:
        if v[i] != count:
            tree[i] = 0
            v[i] = count
        tree[i] += 1
        i += (i&-i)

N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

count = 1
tree1 = [0]*(N+1)
tree2 = [0]*(N+1)
v1 = [0]*(N+1)
v2 = [0]*(N+1)

for i in range(N):
    a,b = A[i],B[i]
    if prefix_sum(tree1,v1,a) != prefix_sum(tree2,v2,b):
        count += 1
    update(tree1,v1,a)
    update(tree2,v2,b)
print(count)