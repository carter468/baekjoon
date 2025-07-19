# 오렌지컵 출제하기
# Gold 2, priority queue, greedy

# 제한이 K문제인 상태에서 하나씩 줄여가며 풀기
import heapq

N,K = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

heap = []
for i in range(N):
    heapq.heappush(heap,(B[i],A[i]))

t = 0
count = [0]*(N+1)
p = [[] for _ in range(N+1)]
for _ in range(K):
    b,a = heapq.heappop(heap)
    count[a] += 1
    heapq.heappush(p[a],-b)
    t += b

result = [-1]*N
for i in range(K-1,N):
    result[i] = t

arr = [set() for _ in range(K+1)]
for i in range(1,N+1):
    arr[count[i]].add(i)

for i in range(K,1,-1):
    f = True
    for idx in arr[i]:
        t += heapq.heappop(p[idx])
        arr[i-1].add(idx)
        while heap:
            b,a = heapq.heappop(heap)
            if count[a] < i-1:
                count[a] += 1
                arr[count[a]].add(a)
                heapq.heappush(p[a],-b)
                t += b
                break
        else:
            f = False
            break
    if f: result[i-2] = t
    else: break
print(*result)

# 제한이 1인 경우부터 하나씩 늘려가면서 넣을 수 있는 문제 추가하며 풀기
import heapq

N,K = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

arr = [[] for _ in range(N+1)]
for i in range(N):
    arr[A[i]].append(B[i])
p = [[] for _ in range(N+1)]
for i in range(1,N+1):
    for j,b in enumerate(sorted(arr[i])):
        p[j+1].append(b)

result = [-1]*(N+1)
heap = []
t = 0
for i in range(1,N+1):
    for b in p[i]:
        heapq.heappush(heap,-b)
        t += b
    while len(heap) > K:
        t += heapq.heappop(heap)
    if len(heap) == K: result[i] = t
print(*result[1:])