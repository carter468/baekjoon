# 나룻배
# Gold 2, implementation, simulation

import sys
input = sys.stdin.readline

m,t,n = map(int,input().split())
p = [[],[]]     # 양쪽 정박장의 승객 정보
for i in range(n):
    a,b = input().split()
    if b == 'left':
        p[0].append((int(a),i))
    else:
        p[1].append((int(a),i))
p[0].sort(reverse=True)
p[1].sort(reverse=True)

time = 0
curr = 0
count = 0
result = [0]*n
while p[0] or p[1]:
    while p[curr] and time >= p[curr][-1][0] and count < m:    # 현재 정박장의 기다리는 승객 탑승
        a,i = p[curr].pop()
        result[i] = time+t
        count += 1
    if count: # 승객 이동
        time += t
        curr ^= 1
        count = 0
    else:    # 대기 승객이 없다
        if not p[curr-1] or p[curr] and p[curr][-1][0] <= p[curr-1][-1][0]: # 현재 정박장 대기
            time = p[curr][-1][0]
        elif p[curr-1]:   # 반대 정박장 이동
            time = max(time,p[curr-1][-1][0])+t
            curr ^= 1
    
print('\n'.join(map(str,result)))