# One-sequence
# Gold 2, ad hoc, constructive

N,S = int(input()),int(input())

x = N*(N-1)//2-S
result = [0]
for i in range(1,N):
    if x >= (N-i)*2:
        x -= (N-i)*2
        result.append(result[-1]-1)
    else:
        result.append(result[-1]+1)

if x == 0:
    print(*result,sep='\n')
else:
    print('NIE')