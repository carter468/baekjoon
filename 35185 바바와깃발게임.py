# 바바와 깃발 게임
# Gold 2, ad hoc

N,L = map(int,input().split())
S = input()

a = b = c = 0
for i in range(L-1):
    if S[i] == 'L':
        c -= 1
    else:
        c += 1
    a = min(a,c)
    b = max(b,c)
if S[-1] == 'L':
    c -= 1
else:
    c += 1

if a <= c <= b or b-a+2 > N:
    print('DEFEAT')
else:
    print('WIN')
    if c < a:
        print(1-c,1)
    else:
        print(N-c,N)