# 최소값과 최대값

# def segmentTree(start,end,idx):
#     if start == end:
#         tree[idx] = [nums[start],nums[start]]
#         return 
#     mid = (start+end)//2
#     segmentTree(start,mid,idx*2)
#     segmentTree(mid+1,end,idx*2+1)
#     tree[idx][0] = min(tree[idx*2][0],tree[idx*2+1][0])
#     tree[idx][1] = max(tree[idx*2][1],tree[idx*2+1][1])
#     return 

# def find(start,end,left,right,idx):
#     if end < left or right < start:
#         return
#     if left <= start and end <= right:
#         ans[0] = min(ans[0],tree[idx][0])
#         ans[1] = max(ans[1],tree[idx][1])
#         return
#     mid = (start+end)//2
#     find(start,mid,left,right,idx*2)
#     find(mid+1,end,left,right,idx*2+1)

# n,m = map(int,input().split())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# tree = [[0,0] for _ in range(n*4)]
# segmentTree(0,n-1,1)

# for _ in range(m):
#     a,b = map(int,input().split())
#     ans = [10*9,1]
#     find(0,n-1,a-1,b-1,1)
#     print(*ans)

import sys
input = sys.stdin.readline

def makemaxtree(start,end,node):
    if start == end:
        maxtree[node] = nums[start]
        return maxtree[node]
    mid = (start+end)//2
    maxtree[node] = max(makemaxtree(start,mid,node*2),makemaxtree(mid+1,end,node*2+1))
    return maxtree[node]
    
def makemintree(start,end,node):
    if start == end:
        mintree[node] = nums[start]
        return mintree[node]
    mid = (start+end)//2
    mintree[node] = min(makemintree(start,mid,node*2),makemintree(mid+1,end,node*2+1))
    return mintree[node]

def findmax(start,end,a,b,node):
    if b<start or a>end:
        return 0
    if a <= start and end <= b:
        return maxtree[node]
    mid = (start+end)//2
    return max(findmax(start,mid,a,b,node*2),findmax(mid+1,end,a,b,node*2+1))

def findmin(start,end,a,b,node):
    if b<start or a>end:
        return 10**9
    if a <= start and end <= b:
        return mintree[node]
    mid = (start+end)//2
    return min(findmin(start,mid,a,b,node*2),findmin(mid+1,end,a,b,node*2+1))

n,m = map(int,input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))
maxtree = [0]*(n*4)
mintree = [0]*(n*4)
makemaxtree(0,n-1,1)
makemintree(0,n-1,1)

for _ in range(m):
    a,b = map(int,input().split())
    print(findmin(0,n-1,a-1,b-1,1),findmax(0,n-1,a-1,b-1,1))