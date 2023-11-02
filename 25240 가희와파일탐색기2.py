# 가희와 파일 탐색기 2
# Gold 3, implementation, hash set

from collections import defaultdict
import sys
input = sys.stdin.readline

u,f = map(int,input().split())

group = defaultdict(list)
for _ in range(u):
    a = input().split()
    if len(a) != 1:
        for g in a[1].split(','):
            group[g].append(a[0])
    group[a[0]].append(a[0])

file = {}
for _ in range(f):
    a = input().split()
    file[a[0]] = (a[1],a[2],a[3])

for _ in range(int(input())):
    a,b,c = input().split()
    if file[b][1] == a: au = file[b][0][0]
    else:
        for u in group[file[b][2]]:
            if a == u:
                au = file[b][0][1]
                break
        else: au = file[b][0][2]
    if c == 'X':
        print(1 if au in ('1','3','5','7') else 0)
    elif c == 'W':
        print(1 if au in ('2','3','6','7') else 0)
    elif c == 'R':
        print(1 if au in ('2','3','4','5','6','7') else 0)