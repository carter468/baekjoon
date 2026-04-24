# 구간과 쿼리
# Gold 5, DFS

interval = []
l = 0

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a == 1:
        interval.append((b,c))
        l += 1
    else:
        q = [b-1]
        visited = [False]*l
        visited[b-1] = True
        while q:
            x = q.pop()
            if x == c-1:
                print(1)
                break
            for nx in range(l):
                x1,y1 = interval[x]
                x2,y2 = interval[nx]
                if (x2 < x1 < y2 or x2 < y1 < y2) and not visited[nx]:
                    visited[nx] = True
                    q.append(nx)
        else: print(0)