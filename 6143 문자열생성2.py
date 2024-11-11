# 문자열 생성 2
# Gold 2, greedy

import sys
input = sys.stdin.readline

def p(c):
    global count
    if count == 80:
        print()
        count = 0
    print(c,end='')
    count += 1

n = int(input())
arr = [input().strip() for _ in range(n)]

count = 0
i,j = 0,n-1
while i <= j:
    a,b = arr[i],arr[j]
    if a < b:
        p(a)
        i += 1
    elif a > b:
        p(b)
        j -= 1
    else:
        ii,jj = i,j
        while jj-ii > 1 and arr[ii] == arr[jj]:
            ii += 1
            jj -= 1
        if arr[ii] < arr[jj]:
            p(a)
            i += 1
        else:
            p(b)
            j -= 1