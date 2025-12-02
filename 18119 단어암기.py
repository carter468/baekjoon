# 단어 암기
# Gold 4, bruteforcing, bitmask

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
word = []
for _ in range(N):
    x = 0
    for c in input().strip():
        x |= 1<<(ord(c)-97)
    word.append(x)

x = (1<<26)-1
for _ in range(M):
    a,b = input().split()
    b = ord(b)-97
    if a == '1':
        x -= 1<<b
    else:
        x |= 1<<b
    count = 0
    for w in word:
        if x&w == w: count += 1
    print(count)