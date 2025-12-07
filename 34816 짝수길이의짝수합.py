# 짝수 길이의 짝수 합
# Gold 5, ad hoc

import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
S = list(input())
for _ in range(Q):
    query = tuple(map(int,input().split()))
    if query[0] == 1:
        i = query[1]
        if S[i-1] == '1': S[i-1] = '0'
        else: S[i-1] = '1'
    else:
        x,y = query[1:]
        if y-x > 2:
            print('YES')
        else:
            s = S[x-1:y]
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    print('YES')
                    break
            else:
                print('NO')