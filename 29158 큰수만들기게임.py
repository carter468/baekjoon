# 큰 수 만들기 게임
# Platinum 4, greedy, number theory

import math

n = int(input())

l = int(math.log2(n-1))
if l == 0: result_jh = 1
elif 2**(l-1)*3 < n: result_jh = int('3'+'2'*(l-1))
else: result_jh = int('2'*l)

factor = []
for i in range(2,int(n**0.5)+1):
    while n%i == 0:
        factor.append(str(i))
        n //= i
if n != 1:
    factor.append(str(n))
f_sort = []
for a in factor:
    f_sort.append((int((a*11)[:11]),a))
result_sh = ''
for a in sorted(f_sort)[::-1]:
    result_sh += a[1]

print(int(result_sh)+result_jh)