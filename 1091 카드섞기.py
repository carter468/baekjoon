# 카드 섞기
# Gold 4, implementation, simulation

n = int(input())
p = list(map(int,input().split()))
s = list(map(int,input().split()))

arr = [0,1,2]*(n//3)
visited = set()
visited.add(tuple(arr))
count = 0
while True:
    if arr == p:
        print(count)
        break

    count += 1
    narr = [0]*n
    for i in range(n):
        narr[i] = arr[s[i]]
    if tuple(narr) in visited:
        print(-1)
        break
    visited.add(tuple(narr))
    arr = narr
