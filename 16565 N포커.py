# N포커
# Gold 2, combinatorics

import math
MOD = 10007

N = int(input())

result = 0
for i in range(1,N//4+1):
    result += math.comb(13,i)*math.comb(52-i*4,N-i*4)%MOD*[-1,1][i%2]

print(result%MOD)