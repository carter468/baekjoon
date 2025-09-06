# Mountains
# Platinum 5, fenwick tree, coordinate compression

def update(i,dif,tree):
    while i <= N:
        tree[i] += dif
        i += (i&-i)

def prefix_sum(i,tree):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

N = int(input())
H = tuple(map(int,input().split()))

dic = dict()
for i,h in enumerate(sorted(set(H))):
    dic[h] = i+1

tree1 = [0]*(N+1)
tree2 = [0]*(N+1)
result = 0
for h in H:
    result += prefix_sum(N,tree2)-prefix_sum(dic[h],tree2)
    update(dic[h],prefix_sum(dic[h]-1,tree1),tree2)
    update(dic[h],1,tree1)
print(result)