# 마작 거신병 9
# Gold 3, constructive, greedy

H = int(input())
W = tuple(map(int,input().split()))
C,D = map(int,input().split())

result = []
for i in range(H):
    result.append([1]*W[i])
prev = W[0]
idx = [0]*H
d = D
for i in range(1,H):
    cur = W[i]
    while cur <= prev:
        if idx[i] == W[i]:
            print(-1)
            exit()
        result[i][idx[i]] = 9
        cur += 8
        idx[i] += 1
        d -= 1
    prev = cur

for _ in range(d):
    if idx[-1] == W[-1]: break
    result[-1][idx[-1]] = 9
    idx[-1] += 1
    d -= 1

h = H-2
if h >= 0:
    prev = sum(result[-1])
    now = sum(result[h])
    while d:
        while h >= 0 and idx[h] == W[h]:
            h -= 1
            prev = now
            now = sum(result[h])

        if h == -1:
            print(-1)
            exit()

        if now+8 < prev:
            result[h][idx[h]] = 9
            now += 8
            d -= 1
            idx[h] += 1
        else:
            h -= 1
            prev = now
            now = sum(result[h])

if d: print(-1)
else:
    for r in result:
        print(*r)