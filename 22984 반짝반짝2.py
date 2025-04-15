# 반짝반짝 2
# Gold 5, probability

N = int(input())
P = tuple(map(float,input().split()))

result = sum(P)
for i in range(1,N):
    result += P[i]*(1-P[i-1])+(1-P[i])*P[i-1]
print(result)