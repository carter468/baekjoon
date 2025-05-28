# 징검다리의 징검다리
# Gold 5, greedy, ad hoc

N,S,E = map(int,input().split())
A = [0]+list(map(int,input().split()))
K = int(input())

x = 0
if S < E:
    for i in range(S-1,0,-1):
        if A[i+1] > 1:
            x += A[i]
        else:
            break
    for i in range(S,E+1):
        x += A[i]
    for i in range(E+1,N+1):
        if A[i-1] > 1:
            x += A[i]
        else:
            break
else:
    for i in range(S+1,N+1):
        if A[i-1] > 1:
            x += A[i]
        else:
            break
    for i in range(S,E-1,-1):
        x += A[i]
    for i in range(E-1,0,-1):
        if A[i+1] > 1:
            x += A[i]
        else:
            break
print(1 if x >= K >= abs(S-E)+1 else 0)