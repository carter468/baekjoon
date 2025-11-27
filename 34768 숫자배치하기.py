# 숫자 배치하기
# Platinum 4, constructive

N = int(input())

if N == 4:
    print(1,8,7,6)
    print(8,7,6,5)
    print(2,3,5,4)
    print(1,2,4,3)
else:
    result = [[1]*N for _ in range(N)]
    n = N*N//2
    dy = 1
    x,y = 0,0
    while n > 1:
        result[x][y] = n
        if y+dy == N or y+dy == -1:
            result[x+3][y] = n
            dy *= -1
            x += 2
        else:
            result[x+1][y+dy] = n
            y += dy
        n -= 1

    for r in result:
        print(*r)