# 래환이의 택시 타기 대작전
# Gold 5, greedy

import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    h,m = input().split(':')
    arr.append(int(h)*60+int(m))

count = 0
c = 0
t = -11
for x in sorted(arr):
    if x-10 <= t:
        c += 1
        if c == 3:
            c = 0
            t = -11
    else:
        c = 1
        t = x+10
        count += 1
print(count)