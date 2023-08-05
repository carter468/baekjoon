# 자리수로 나누기
# Gold 5, bruteforce

from collections import deque

n = int(input())
q = deque([n])
while 1:
    x = q.popleft()
    for a in str(n):
        if a != '0' and x%int(a): break
    else:
        print(x)
        break
    for i in range(10):
        q.append(x*10+i)