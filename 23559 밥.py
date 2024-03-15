# 밥
# Gold 5, greedy

import sys
input = sys.stdin.readline

n,x = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x:x[1]-x[0])

k = (x//1000-n)//4
print(sum([max(a,b) for a,b in arr[:k]])+sum([b for a,b in arr[k:]]))