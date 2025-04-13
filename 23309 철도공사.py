# 철도 공사
# Gold 4, implementation, linked list

import os, io, __pypy__
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
ans = __pypy__.builders.StringBuilder()

def main():
    N, M = map(int,input().decode().split())
    arr = list(map(int,input().decode().split()))

    forward = [0]*1000001
    backward = [0]*1000001

    for i in range(N):
        forward[arr[i-1]] = arr[i]
        backward[arr[i]] = arr[i-1]

    for _ in range(M):
        query = input().decode().split()
        if query[0] == 'BN':
            i,j = int(query[1]),int(query[2])
            k = forward[i]
            forward[i],backward[j] = j,i
            forward[j],backward[k] = k,j
            ans.append(str(k)+'\n')
        elif query[0] == 'BP':
            i, j = int(query[1]),int(query[2])
            k = backward[i]
            forward[j],backward[i] = i,j
            forward[k],backward[j] = j,k
            ans.append(str(k)+'\n')
        elif query[0] == 'CN':
            i = int(query[1])
            j = forward[i]
            ans.append(str(j)+'\n')
            k = forward[j]
            forward[i],backward[k] = k,i
        elif query[0] == 'CP':
            i = int(query[1])
            j = backward[i]
            ans.append(str(j)+'\n')
            k = backward[j]
            forward[k],backward[i] = i,k

    os.write(1,ans.build().encode())

if __name__ == '__main__':
    main()