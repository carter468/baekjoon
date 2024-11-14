# 더 푸르게
# Gold 3, implementation, bruteforcing, bitmask

D = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
N = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]

def check():
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'K':
                for di,dj in D:
                    ni,nj = i+di,j+dj
                    if 0 <= ni < h and 0 <= nj < w and board[ni][nj] != 'E':
                        return False
            elif board[i][j] == 'Q':
                for di,dj in D:
                    ni,nj = i+di,j+dj
                    while 0 <= ni < h and 0 <= nj < w:
                        if board[ni][nj] != 'E': 
                            return False
                        ni += di
                        nj += dj
            elif board[i][j] == 'R':
                for di,dj in D[:4]:
                    ni,nj = i+di,j+dj
                    while 0 <= ni < h and 0 <= nj < w:
                        if board[ni][nj] != 'E': 
                            return False
                        ni += di
                        nj += dj
            elif board[i][j] == 'B':
                for di,dj in D[4:]:
                    ni,nj = i+di,j+dj
                    while 0 <= ni < h and 0 <= nj < w:
                        if board[ni][nj] != 'E': 
                            return False
                        ni += di
                        nj += dj
            elif board[i][j] == 'N':
                for di,dj in N:
                    ni,nj = i+di,j+dj
                    if 0 <= ni < h and 0 <= nj < w and board[ni][nj] != 'E':
                        return False
    return True

while True:
    try:
        input()
        w,h = int(input()),int(input())
        arr = [input().split() for _ in range(h)]
        piece = []
        for i in range(h):
            for j in range(w):
                if arr[i][j] != 'E':
                    piece.append((i,j,arr[i][j]))
        input()
        
        l = len(piece)
        result = 15
        for i in range(1<<l):
            board = [['E']*w for _ in range(h)]
            count = 0
            for j in range(l):
                if i>>j&1:
                    a,b,c = piece[j]
                    board[a][b] = c
                else:
                    count += 1
            if check(): result = min(result,count)

        print(f'Minimum Number of Pieces to be removed: {result}')

    except:
        break