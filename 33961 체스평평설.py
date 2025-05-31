# 체스평평설
# Gold 5, ad hoc, constructive, case work

if (M:=int(input())) <= 2: print('NO')
else:
    print('YES')
    visited = [[False]*M for _ in range(2)]
    visited[0][0] = True
    print(1,1)
    x,y,d = 0,0,0
    c = 1
    while c < 2*M:
        nx = 1-x
        if d == 0:
            if y+2 < M and not visited[nx][y+2]:
                visited[nx][y+2] = True
                x,y = nx,y+2
                c += 1
                print(x+1,y+1)
            elif y+1 < M and not visited[nx][y+1]:
                visited[nx][y+1] = True
                x,y = nx,y+1
                c += 1
                print(x+1,y+1)
            else:
                d = 1
        else:
            if y-2 >= 0 and not visited[nx][y-2]:
                visited[nx][y-2] = True
                x,y = nx,y-2
                c += 1
                print(x+1,y+1)
            elif y-1 >= 0 and not visited[nx][y-1]:
                visited[nx][y-1] = True
                x,y = nx,y-1
                c += 1
                print(x+1,y+1)
            else:
                d = 0