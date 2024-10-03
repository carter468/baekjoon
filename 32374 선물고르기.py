# 선물 고르기
# Gold 4, greedy

from collections import defaultdict

n,k = map(int,input().split())
a = sorted(map(int,input().split()))
b = sorted(map(int,input().split()))

dic = defaultdict(int)
for c in map(int,input().split()):
    dic[c] += 1

for x in b[::-1]:
    if dic[x] == 0:
        for y in a[::-1]:
            if y <= x:
                print(y)
                exit()
    dic[x] -= 1
