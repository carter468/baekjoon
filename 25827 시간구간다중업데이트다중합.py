# 시간 구간 다중 업데이트 다중 합
# Gold 5, prefix sum, IMOS

import sys
input = sys.stdin.readline

def sec(x):
    h,m,s = map(int,x.split(':'))
    return h*3600+m*60+s

arr = [0]*86444
f = False
for _ in range(int(input())):
    a,b,c = input().split()
    if a == '1':
        i,j = sec(b),sec(c)
        arr[i] += 1
        arr[j] -= 1
    else:
        if f == False:
            for i in range(86400):
                arr[i+1] += arr[i]
            for i in range(86400):
                arr[i+1] += arr[i]
            f = True
        i,j = sec(b),sec(c)
        print(arr[j-1]-arr[i-1])
