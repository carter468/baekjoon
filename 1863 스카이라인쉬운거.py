# 스카이라인 쉬운거
# Gold 4, stack

import sys
input = sys.stdin.readline

arr = [True]+[False]*500000
q = [0]
count = 0
for i in range(int(input())):
    _,y = map(int,input().split())
    while y < q[-1]:
        arr[q.pop()] = False
    if not arr[y]:
        count += 1
        arr[y] = True
        q.append(y)
print(count)