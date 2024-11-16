# A flea on a chessboard
# Gold 5, implementation

while True:
    S,x,y,dx,dy = map(int,input().split())
    if S == 0: break

    arr = [[False]*(S+1) for _ in range(S+1)]
    count = 0
    xx,yy = x,y
    while True:
        xx %= S*2
        yy %= S*2
        a,b = divmod(xx,S)
        c,d = divmod(yy,S)
        if b and d and (a+c)%2:
            print(f'After {count} jumps the flea lands at ({x}, {y}).')
            break
        if xx > S or yy > S:
            xx -= S
            yy -= S
            if xx < 0: xx = S
            if yy < 0: yy = S
        if arr[xx][yy]:
            print('The flea cannot escape from black squares.')
            break
        arr[xx][yy] = True
        count += 1
        x += dx
        y += dy
        xx += dx
        yy += dy