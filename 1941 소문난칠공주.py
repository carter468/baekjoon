# 소문난 칠공주
# Gold 3, bruteforcing

def select(s,l,c):
    global count
    if c == 7:
        if check(s): count += 1
        return
    for i in range(l,25):
        if not (s>>i)&1: select(s|(1<<i),i,c+1)

def check(s):
    p = set()
    for i in range(25):
        if (s>>i)&1: p.add((i//5,i%5))
    x,y = p.pop()
    cs = 1 if arr[x][y] == 'S' else 0
    visited = {(x,y)}
    q = [(x,y)]
    while q:
        x,y = q.pop()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) in p and (nx,ny) not in visited:
                if arr[nx][ny] == 'S': cs += 1
                visited.add((nx,ny))
                q.append((nx,ny))
                if len(visited) == 7: return True if cs >= 4 else False
    return False

arr = [input() for _ in range(5)]
count = 0
select(0,0,0)
print(count)