# Family
# Gold 4, disjoint set

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if x not in parent:
        parent[x] = x
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

parent = defaultdict()
for _ in range(int(input())):
    name1,connection,name2 = input().split()
    name1,name2 = find(name1),find(name2)
    parent[name1] = name2

for _ in range(int(input())):
    name1,name2 = map(find,input().split())
    print('Related' if name1 == name2 else 'Not Related')