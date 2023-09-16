# 수열 섞기
# Gold 3, deque, greedy

# 더 깔끔하게 구현 해보기 2~3가지 수정가능

from collections import deque

input()
pos,neg,zero = [],[],[]
for a in map(int,input().split()):
    if a == 0: zero.append(0)
    elif a > 0: pos.append(a)
    else: neg.append(a)
pos.sort()
neg.sort()

pr,nr = deque(),deque()
po,no = 1,1
for a in pos[::-1]:
    if po == 1:
        pr.append(a)
        po = 0
    else:
        pr.appendleft(a)
        po = 1
for a in neg:
    if no == 1:
        nr.append(a)
        no = 0
    else:
        nr.appendleft(a)
        no = 1

if pr and pr[0] < pr[-1]: pr.reverse()
if nr and nr[0] < nr[-1]: nr.reverse()
print(*pr,*zero,*nr)