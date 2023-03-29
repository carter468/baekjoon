# 배수 찾기
# Gold 1, BFS

from collections import deque
import sys
input = sys.stdin.readline

while n:=int(input()):
    q = deque([1])
    while 1:
        x = q.popleft()
        if x%n == 0:
            print(x)
            break
        q.append(10*x)
        q.append(10*x+1)