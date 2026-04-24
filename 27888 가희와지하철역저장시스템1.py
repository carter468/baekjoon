# 가희와 지하철역 저장 시스템 1
# Gold 2, implementation

import sys
input = sys.stdin.readline

def U():
    s = query[i][1]
    x = 0
    for f in query[i][2]:
        x += 1<<num[f]
    count[x] = count.get(x,0)+1
    count[station[s]] -= 1
    station[s] = x

def G():
    c = 0
    for key in count:
        for f in query[i][1]:
            if f not in num:
                print(0)
                return
            if key>>num[f]&1 == 0: break
        else:
            c += count[key]
    print(c)

station = dict()
for _ in range(int(input())):
    station[input().strip()] = 0

Q = int(input())
query = [input().split() for _ in range(Q)]
feature = set()
for i in range(Q):
    if query[i][0] == 'U':
        query[i][2] = query[i][2].split(',')
        feature.update(query[i][2])
    else:
        query[i][1] = query[i][1].split(',')

num = dict()
for i,f in enumerate(feature):
    num[f] = i

count = {0:0}
for i in range(Q):
    if query[i][0] == 'U':
        U()
    else:
        G()