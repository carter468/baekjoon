# DSLR

from collections import deque
import sys
input = sys.stdin.readline

def D(x):
    return (x*2)%10000
def S(x):
    return (x-1)%10000
def L(x):
    return (x%1000)*10 + x//1000
def R(x):
    return (x%10)*1000 + (x//10)

def bfs(a,b):               # 너비 우선 탐색
    visited = [0]*10000     # 방문 여부      
    q = deque()
    q.append((a,''))            
    while q:
        num,path = q.popleft()
        visited[num] = 1
        if num == b:          # 원하는 숫자
            print(path)
            return
        for i in ('D','S','L','R'):
            if i=='D':
                k = D(num)
            elif i=='S':
                k = S(num)
            elif i=='L':
                k = L(num)
            else:
                k = R(num)
            if visited[k] == 0:
                visited[k] = 1
                q.append((k,path+i))  

T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    bfs(A,B)