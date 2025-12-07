# Yonsei TOTO 2
# Gold 5, greedy

N,M,S = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

arr = sorted([((B[i]/A[i],i)) for i in range(N)])
result = [0]*N
while arr and S > 0:
    _,i = arr.pop()
    result[i] = min(A[i],S,M)
    S -= min(A[i],S,M)
print(*result)