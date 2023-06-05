# 명상방해꾼
# Gold 5, 브루트포스

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

mental = [0]*m
bird = []
for _ in range(n):
    a,b = input().split()
    a = -1 if a == 'L' else 1
    bird.append((a,b))
    count = 0
    for i,c in enumerate(b):
        if c == '1': count += 1
        mental[i] += a*count

result = (0,sys.maxsize)
for i in range(n):
    count,temp = 0,0
    for j,c in enumerate(bird[i][1]):
        if c == '1': count += 1
        k = mental[j]-bird[i][0]*count
        temp = max(temp,abs(k)) 
    if temp < result[1]:
        result = (i+1,temp)

print('\n'.join(map(str,result)))