# 수 묶기
# Gold 4, greedy

import sys
input = sys.stdin.readline

po,ne,ze = [],[],1
for _ in range(int(input())):
    x = int(input())
    if x > 0: po.append(x)
    elif x < 0: ne.append(-x)
    else: ze = 0

result = 0
po.sort()
ne.sort()

while len(po) >= 2:
    x,y = po.pop(),po.pop()
    if y == 1: result += x+y
    else: result += x*y
if po: result += po.pop()

while len(ne) >= 2:
    x,y = ne.pop(),ne.pop()
    result += x*y
if ne: result -= ne.pop()*ze

print(result)