# 주문은 토기입니까?
# Gold 4, greedy, deque

from collections import deque

N,M = map(int,input().split())
arr = tuple(map(int,input().split()))

now = 0 # 마지막 서빙한 시간+1
a,b = deque(),deque() # 토기만들수있는시각, 커피담을수있는시각
for t in arr:
    b += list(range(now,t))
    
    if a: # 토기만들수있는시간이 존재한다면 가장 빠른 시각에 만든다.
        a.popleft()
    else: # 없다면 커피담을수있는시간이 존재한다면 가장 빠른 시각에 만든다.
        if not b: exit(print('fail'))
        b.popleft()

    # 커피담을시간은 b에서 가능한 가장 빠른 시각에 담는다.
    # 서빙하기전에 흙탕물이 되는 시각들은 토기만들수있는 시각으로 빼놓는다.
    while True:
        if not b: exit(print('fail'))
        x = b.popleft()
        if x+M >= t: break
        a.append(x)
    now = t+1
print('success')