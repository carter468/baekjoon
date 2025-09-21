# Ian Sequences
# Platinum 5, ad hoc, constructive

N = int(input())

m = N%2
print(*range(N,0,-2),end=' ')
if m == 1:
    print(1,end=' ')
for i in range(N//2):
    a = i*2+1+m
    print(a,a+1,a,end=' ')