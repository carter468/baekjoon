# 장미
# Gold 4, math, bruteforcing

N,A,B,C,D = map(int,input().split())

if B*C < A*D: A,B,C,D = C,D,A,B

result = 10**18
for a in range(C):
    c = (N-a*A-1)//C+1
    result = min(result,a*B+max(0,c)*D)
    if c < 0: break

print(result)