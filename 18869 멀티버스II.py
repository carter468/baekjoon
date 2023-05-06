# 멀티버스 II
# Gold 5, 좌표압축

import sys
input = sys.stdin.readline

m,_ = map(int,input().split())
multiverse = []
for _ in range(m):
    planet = tuple(map(int,input().split()))
    sorted_planet = sorted(set(planet))
    rank = {}
    for i in range(len(sorted_planet)):
        rank[sorted_planet[i]] = i
    multiverse.append([rank[i] for i in planet])

count = 0
for i in range(m):
    for j in range(i+1,m):
        count += (multiverse[i] == multiverse[j])
print(count)