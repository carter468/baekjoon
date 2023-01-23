# 수열의 점수
# Gold 4, 그리디 알고리즘

import sys
input = sys.stdin.readline

a = []  # 2 이상의 양수
b = []  # 음수
c = False   # 0의 존재
score = 0
for _ in range(int(input())):
    n = int(input())
    if n>1:
        a.append(n)
    elif n==1:
        score += 1  # 1의 개수
    elif n<0:
        b.append(n)
    else:
        c = True
a.sort()
b.sort(reverse=True)

while len(a)!=0:
    try:
        x = a.pop()
        y = a.pop()
        score += x*y
    except:
        score += x

while len(b)!=0:
    try:
        x = b.pop()
        y = b.pop()
        score += x*y
    except:
        if not c:
            score += x

print(score)