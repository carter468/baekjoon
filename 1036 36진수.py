# 36진수
# Gold 1, 그리디 알고리즘, 수학

from collections import defaultdict
import sys
input = sys.stdin.readline
chr2num = {chr(i+65):i+10 for i in range(26)}
for i in range(10):
    chr2num[str(i)] = i

result = 0
increment = defaultdict(int)
for _ in range(int(input())):
    a = input().strip()
    for i,b in enumerate(a[::-1]):
        j = 36**i
        result += chr2num[b]*j
        increment[b] += (35-chr2num[b])*j

for a,b in sorted(increment.items(),key=lambda x:x[1],reverse=True)[:int(input())]:
    result += b
answer = ''
while result>0:
    result,r = divmod(result,36)
    if r>=10:
        answer += chr(65+r-10)
    else:
        answer += str(r)

print(answer[::-1] if answer else 0)