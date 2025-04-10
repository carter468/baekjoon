# 가짜 금화 찾기
# Gold 4, ternary search

import sys

l,r = 1,int(input())
for _ in range(5):
    if l+1 == r:
        print('?',l,0,r,0)
        sys.stdout.flush()
        if input() == '>': exit(print('!',r))
        else: exit(print('!',l))

    c = (r-l+1)//3
    print('?',end=' ')
    for i in range(c):
        print(l+i,end=' ')
    print('0',end=' ')
    for i in range(c):
        print(r-i,end=' ')
    print('0')

    sys.stdout.flush()
    x = input()
    if x == '>': l = r-c+1
    elif x == '<': r = l+c-1
    else: l,r = l+c,r-c

    if l == r: exit(print('!',l))