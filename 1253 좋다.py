# 좋다
# Gold 4, data structure

from collections import defaultdict

def solve():
    for j in range(n):
        if i == j: continue
        for idx in dic[arr[i]-arr[j]]:
            if idx != i and idx != j: return True
    return False

n = int(input())
arr = tuple(map(int,input().split()))
dic = defaultdict(list)
for i,a in enumerate(arr):
    dic[a].append(i)
count = 0
for i in range(n):
    if solve(): count += 1
print(count)
