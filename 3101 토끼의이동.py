# 토끼의 이동
# Gold 3, math, implementation

def find(i,j):
    return (i+j)*(i+j+1)//2+1+(j if (i+j)%2 == 0 else i)

N,K = map(int,input().split())
move = {'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}
result,x,y = 1,0,0
for a in input():
    x += move[a][0]
    y += move[a][1]
    if x+y >= N:
        result += N*N+1-find(N-x-1,N-y-1)
    else:
        result += find(x,y)
print(result)