# 수식 고치기
# Gold 5, case work

T = {'T':1,'F':0}

N = int(input())
A = input().split()
C = input()

x = T[A[0]]
for i in range(N//2-1):
    o = A[i*2+1]
    y = T[A[i*2+2]]
    if o == '&':
        x &= y
    else:
        x |= y

if N == 1:
    print(0 if A[0] == C else 1)
else:
    o = A[-2]
    y = T[A[-1]]

    if o == '&':
        if C == 'T':
            print([x,y].count(0))
        else:
            print(x&y)
    else:
        if C == 'T':
            print(1-(x|y))
        else:
            print([x,y].count(1))