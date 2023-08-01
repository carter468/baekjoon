# 더하기와 나누기
# Gold 5, math, constructive

n = int(input())

if n == 2:
    print(2,4)
else:
    s = n*n-n
    for i in range(3,10**6,2):
        if s%i == 0:
            print(i,*list(range(2,n*2,2)))
            break