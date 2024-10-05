# 초콜릿 괴도 코코 (Sweet)
# Gold 2, bruteforcing, DFS

def isTree():
    visited = [[False]*n for _ in range(n)]
    f = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#' and not visited[i][j]:
                if f: return False
                f = True
                visited[i][j] = True
                q = [(i,j,i,j)]
                while q:
                    x,y,px,py = q.pop()
                    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '#':
                            if (nx,ny) != (px,py) and visited[nx][ny]:
                                return False
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx,ny,x,y))

    for x in range(n):
        for y in range(n):
            if arr[x][y] == '#' and not visited[x][y]:
                return False
    return True

n = int(input())
arr = [list(input()) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '#':
            arr[i][j] = '.'
            if isTree(): result.append((i+1,j+1))
            arr[i][j] = '#'

print(len(result))
for r in result:
    print(*r)
