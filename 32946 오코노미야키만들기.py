# 오코노미야키 만들기
# Gold 3, case work

N = int(input())
p1,p2 = map(int,input().split())
M = int(input())
S = int(input())

if (M-p1)%2 == 0 and (M-p2)%2 == 0: print(-1)
else:
    answer = 10**9
    if (M-p1)%2 == 1:
        if p2 > M:
            c = abs(M-p1)
            if S < p2:
                c += abs(M-S)
                answer = min(answer,c)
            elif S != N:
                c += (S+1-p2)+S-M
                answer = min(answer,c)
        elif (M-p2)%2 == 0 and M != N:
            p3 = M+1
            c = M-p1+(p3-p2)
            if S < p3:
                c += abs(M-S)
                answer = min(answer,c)
            elif S != N:
                c += (S+1-p3)+S-M
                answer = min(answer,c)
    if (M-p2)%2 == 1:
        if M > p1:
            c = abs(M-p2)
            if S > p1:
                c += abs(M-S)
                answer = min(answer,c)
            elif S != 1:
                c += M-S+p1-(S-1)
                answer = min(answer,c)
        elif (M-p1)%2 == 0 and M != 1:
            p3 = M-1
            c = p2-M+p1-p3
            if S > p3:
                c += abs(M-S)
                answer = min(answer,c)
            elif S != 1:
                c += M-S+p3-(S-1)
                answer = min(answer,c)
    print(answer if answer != 10**9 else -1)