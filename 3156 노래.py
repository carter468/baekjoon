# 노래
# Gold 5, sorting, data structure

from collections import defaultdict

arr = []
for _ in range(int(input())):
    _,_,a,*b = input().split()
    for c in b:
        arr.append((int(a),c))

result = defaultdict(list)
visited = set()
for a,c in sorted(arr):
    if c not in visited:
        visited.add(c)
        result[a].append(c)

count = 1
for i in range(1,101):
    if len(result[i]) == 1 and count == i:
        print(i,*result[i])
    count += len(result[i])