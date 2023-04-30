# 핑거 스냅
# Gold 5, BFS, 소수판정

from collections import deque
import sys
input = sys.stdin.readline
MAX = 1000001

def check(a,b):
    for i in seive[a:b+1]:
        if i:
            return False
    return True

seive = [1]*MAX
for i in range(2,int(MAX**0.5)+1):
    if seive[i]:
        for j in range(i*i,MAX,i):
            seive[j] = 0

for _ in range(int(input())):
    n,a,b = map(int,input().split())

    if check(a,b):
        print(-1)
        continue

    visit = [-1]*MAX
    visit[n] = 0
    q = deque([n])
    while 1:
        x = q.popleft()
        if a <= x <= b and seive[x]:
            print(visit[x])
            break
        for nx in (x//2,x//3,x+1,x-1):
            if nx < 1 or nx >= MAX or visit[nx] != -1: continue
            visit[nx] = visit[x]+1
            q.append(nx)