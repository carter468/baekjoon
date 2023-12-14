# 케이크 자르기 2
# Gold 2, DP

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def left(l): return (l-1)%n
def right(r): return (r+1)%n

def ioi(l,r):
    if right(r) == l: return 0
    if arr[left(l)] > arr[right(r)]: return joi(left(l),r)
    else: return joi(l,right(r))

def joi(l,r):
    if dp[l][r] != -1: return dp[l][r]
    if right(r) == l: return 0
    dp[l][r] = max(ioi(left(l),r)+arr[left(l)],ioi(l,right(r))+arr[right(r)])
    return dp[l][r]

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

print(max([arr[i]+ioi(i,i) for i in range(n)]))