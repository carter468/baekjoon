# A-머신
# Gold 4, implementation, simulation

state = input()
N,L = map(int,input().split())
rule = [input().split() for _ in range(N)]
S = list(input())

i = 0
v = set()
while True:
    s = S[i]
    for a,b,c,d,e in rule:
        if (a,b) == (state,s):
            state = d
            S[i] = c
            i += int(e)
            break
    else: exit(print('STOP'))
    ss = ''.join(S)
    if (ss,i,state) in v: exit(print('CONTINUE'))
    v.add((ss,i,state))
    if i < 0 or i == L: exit(print('STOP'))