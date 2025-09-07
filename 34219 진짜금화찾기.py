# 진짜 금화 찾기
# Gold 3, ad hoc

import sys
input = sys.stdin.readline

N = int(input())

arr = list(range(1,N+1))
for _ in range(3):
    bucket = [[] for _ in range(6)]
    query = [0]*(N+1)
    for i,a in enumerate(arr):
        bucket[i%6].append(a)
        query[a] = i%6

    print('?',*query[1:])
    sys.stdout.flush()
    arr = bucket[int(input())-sum(query)*9]

print('!',*arr)