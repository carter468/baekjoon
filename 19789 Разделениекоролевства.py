# Разделение королевства
# Gold 5, constructive

from collections import defaultdict
import sys
input = sys.stdin.readline

x = set()
y = defaultdict(list)
for _ in range(int(input())):
    a,b = map(int,input().split())
    x.add(a)
    y[a].append(b)

result = set()
x = sorted(x)
for i in range(len(x)-1):
    result.add(('x',x[i+1]))
for x in y:
    arr = sorted(y[x])
    for i in range(len(arr)-1):
        result.add(('y',arr[i+1]))

print(len(result))
for r in result:
    print(*r)