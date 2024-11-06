# 월요일-토요일
# Gold 5, number theory

while True:
    n = int(input())
    if n == 1: break

    seive = [-1]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            for j in (i,n//i):
                if j%7 in (1,6) and seive[j] == -1:
                    seive[j] = 1
                    for k in range(j*2,n+1,j):
                        seive[k] = 0
    if seive[n] == -1 and n%7 in (1,6): seive[n] = 1
    
    print(f'{n}: ',end='')
    for i in range(2,n+1):
        if seive[i] == 1: print(i,end=' ')
    print()