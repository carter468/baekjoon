# 수열과 쿼리 15
# Gold 3, priority queue, segtree

# priority queue, 380ms
import sys,heapq
input = sys.stdin.readline

n = int(input())
arr = [0]+list(map(int,input().split()))

heap = []
for i in range(1,n+1):
    heapq.heappush(heap,(arr[i],i))

heap_r = []
for _ in range(int(input())):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        heapq.heappush(heap_r,(arr[q[1]],q[1]))
        arr[q[1]] = q[2]
        heapq.heappush(heap,(q[2],q[1]))
    else:
        while heap_r and heap_r[0] == heap[0]:
            heapq.heappop(heap_r)
            heapq.heappop(heap)
        print(heap[0][1])

# segtree, 880ms
import sys
input = sys.stdin.readline

def init_tree(left,right,node):
    if left == right:
        tree[node] = (arr[left],left)
    else:
        mid = (left+right)//2
        init_tree(left,mid,node*2)
        init_tree(mid+1,right,node*2+1)
        tree[node] = min(tree[node*2],tree[node*2+1])

def update(left,right,node,i,v):
    if i < left or i > right: return
    if left == right:
        tree[node] = (v,left)
        return
    
    mid = (left+right)//2
    update(left,mid,node*2,i,v)
    update(mid+1,right,node*2+1,i,v)
    tree[node] = min(tree[node*2],tree[node*2+1])

n = int(input())
arr = [0]+list(map(int,input().split()))

tree = [0]*(n*4)
init_tree(1,n,1)

for _ in range(int(input())):
    q = tuple(map(int,input().split()))
    if q[0] == 2:
        print(tree[1][1])
    else:
        update(1,n,1,q[1],q[2])