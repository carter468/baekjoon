# 선분 덮기
# Gold 3, 스위핑

import sys
input = sys.stdin.readline

M = int(input())
line = []
while True:
    line.append(tuple(map(int,input().split()))) 
    if line[-1]==(0,0):
        break

left,right = -50000,0
temp = 0
answer = 0
for l,r in sorted(line):
    if left<l<=right:
        if temp <= r:
            temp = r
        if r>=M:
            right=M
            answer += 1
            break
    else:
        if right>temp:
            break
        answer += 1
        left,right = right, temp

print(answer if right==M else 0)