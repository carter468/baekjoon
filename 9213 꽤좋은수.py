# 꽤 좋은 수 
# Gold 2, 수학

import sys
input = sys.stdin.readline

MAX = 10**6
divisor_sum = [i-1 for i in range(MAX)]
for i in range(2,MAX):
    for j in range(i*2,MAX,i):
        divisor_sum[j] -= i

idx = 1
while True:
    s,e,b = map(int,input().split())
    if s==0:
        break
    count = 0
    for i in divisor_sum[s:e+1]:
        if abs(i)<=b:
            count += 1
    print(f'Test {idx}: {count}')
    idx += 1