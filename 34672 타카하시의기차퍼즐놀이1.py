# 타카하시의 기차 퍼즐 놀이 1
# Gold 5, ad hoc

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    R,C,K = map(int,input().split())

    c = 2**(C//3)
    if R == 1 or C%3 != 0 or K > c:
        print(-1)
        continue
    
    res1 = []
    res2 = []
    c //= 2
    while c:
        if K > c:
            res1 += [3,2,2]
            res2 += [3,3,2]
            K -= c
        else:
            res1 += [1,1,4]
            res2 += [1,4,4]
        c //= 2
    
    print(''.join(map(str,res1)))
    print(''.join(map(str,res2)))