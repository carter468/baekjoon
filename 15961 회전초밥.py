# 회전 초밥
# Gold 4, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
dish = [0]*(d+1)
table = [int(input()) for _ in range(n)]
for i in range(k-1):
    table.append(table[i])

dish[c] = 1
count = 1
for i in table[:k]:
    dish[i] += 1
    if dish[i] == 1:
        count += 1
result = count
for i in range(n-1):
    dish[table[i]] -= 1
    if dish[table[i]] == 0:
        count -= 1
    dish[table[i+k]] += 1
    if dish[table[i+k]] == 1:
        count += 1
    result = max(result,count)
    
print(result)