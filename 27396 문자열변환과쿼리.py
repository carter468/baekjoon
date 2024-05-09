# 문자열 변환과 쿼리
# Gold 5, hash_set

import sys

dic = {}
for i in range(26):
    dic[chr(i+65)] = chr(i+65)
    dic[chr(i+97)] = chr(i+97)

s,n = input().split()
for _ in range(int(n)):
    q = sys.stdin.readline().split()
    if q[0] == '1':
        a,b = q[1:]
        for key in dic:
            if dic[key] == a: dic[key] = b
    else:
        for c in s:
            print(dic[c],end='')
        print()