# John's Math Problem
# Gold 1, math, combinatorics

MOD = 998244353

N = input()

l = len(N)
result = 0
for i in range(l):
    result += int(N[i])*pow(2,i,MOD)*pow(11,l-i-1,MOD)
print(result%MOD)