# Not Equal
# Gold 5, greedy

N = int(input())

visited = [[False]*(N+1) for _ in range(N+1)]
visited[N][1] = True
result = ['a1']
x = 1
for _ in range(N*(N-1)//2):
    for nx in range(1,N+1):
        if nx != x and not visited[x][nx]:
            visited[x][nx] = True
            visited[nx][x] = True
            result.append(f'a{nx}')
            x = nx
            break

print(*result,'a1')