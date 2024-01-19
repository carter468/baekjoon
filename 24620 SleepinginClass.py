# Sleeping in Class
# Gold 3, number theory, prefix sum

for _ in range(int(input())):
    n = int(input())
    arr = [0]+list(map(int,input().split()))
    for i in range(n):
        arr[i+1] += arr[i]
    k = arr[-1]

    f = []
    for i in range(1,int(k**0.5)+1):
        if k%i == 0:
            f.append(i)
            if i*i != k:
                f.append(k//i)

    result = 0
    for i in sorted(f):
        l,r,c = 0,1,0
        while r <= n:
            if arr[r]-arr[l] == i:
                c += r-l-1
                l,r = r,r+1
            elif arr[r]-arr[l] < i:
                r += 1
            else: break
        else:
            if l == n: result = c
            break
    print(result)