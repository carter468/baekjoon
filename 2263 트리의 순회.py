# 트리의 순회

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def preorder(in_start,in_end,post_start,post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    parents = postorder[post_end]
    print(parents,end=' ')

    left = posi[parents] - in_start
    right = in_end - posi[parents]

    preorder(in_start,in_start+left-1,post_start,post_start+left-1)
    preorder(in_end-right+1,in_end,post_end-right,post_end-1)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

posi = [0]*(n+1)
for i in range(n):
    posi[inorder[i]] = i

preorder(0,n-1,0,n-1)