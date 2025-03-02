# Kocka
# Gold 5, implementation

cube = [[0,5,list('+---+')],[0,6,list('|   |/')],[0,7,list('|   | +')],
        [0,7,list('+---+ |')],[1,7,list('/   /|')],[2,7,list('+---+')]]

M,N = map(int,input().split())
arr = []
x = 0
for i in range(M):
    arr.append(tuple(map(int,input().split())))
    x = max(x,3*max(arr[-1])+3+2*(M-1-i))
y = 1+4*N+2*M

result = [['.']*y for _ in range(x)]
for i in range(M):
    for j in range(N):
        sy = (M-1-i)*2+j*4
        for k in range(arr[i][j]):
            sx = -((M-1-i)*2+k*3+1)
            for l in range(6):
                a,b,c = cube[l]
                result[sx-l][sy+a:sy+b] = c

for r in result:
    print(''.join(r))