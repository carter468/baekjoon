# Cube IV (Large)
# Gold 4, bruteforcing

import sys
input = sys.stdin.readline

for t in range(int(input())):
    while True:
        if S:=input().strip(): break
    S = int(S)
    arr = [input().split() for _ in range(S)]

    dic = {S*S+1:(-1,-1)}
    for i in range(S):
        for j in range(S):
            dic[int(arr[i][j])] = (i,j)
    
    result = [0,0]
    s,l,x,y = 0,0,-1,-1
    for i in range(1,S*S+2):
        nx,ny = dic[i]
        if abs(x-nx)+abs(y-ny) == 1:
            l += 1
        else:
            if l > result[1]:
                result = [s,l]
            s,l = i,1
        x,y = nx,ny
    
    print(f'Case #{t+1}:',*result)