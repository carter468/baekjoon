# 아리스, 청소합니다!
# Gold 3, implementation, simulation

M = ((-1,0),(0,1),(1,0),(0,-1))

h,w = map(int,input().split())
r,c,d = map(int,input().split())
A = [list(map(int,input())) for _ in range(h)]
B = [list(map(int,input())) for _ in range(h)]

state = [[True]*w for _ in range(h)]
result = 0
count = 0
while True:
    if r < 0 or r == h or c < 0 or c == w: break
    count += 1
    if state[r][c]:
        state[r][c] = False
        d = (d+A[r][c])%4
        r += M[d][0]
        c += M[d][1]
        result = count
        prev = r,c,d
    else:
        d = (d+B[r][c])%4
        r += M[d][0]
        c += M[d][1]
        if (r,c,d) == prev: break
print(result)