# Subsequences Summing to Sevens
# Gold 5, prefix_sum

import sys
input = sys.stdin.readline

idx = [[0]]+[[] for _ in range(6)]
c,result = 0,0
for i in range(int(input())):
    c = (c+int(input()))%7
    idx[c].append(i+1)
    result = max(result,idx[c][-1]-idx[c][0])
print(result)