# 작은 벌점
# Gold 5, greedy

A,B,C = map(int,input().split())

arr1 = sorted(map(int,input().split()))
arr2 = sorted(map(int,input().split()))
arr3 = sorted(map(int,input().split()))

result = 10**10
a,b,c = 0,0,0
while True:
    x,y,z = arr1[a],arr2[b],arr3[c]
    result = min(result,max(x,y,z)-min(x,y,z))

    if min(x,y,z) == x and a < A-1:
        a += 1
    elif min(x,y,z) == y and b < B-1:
        b += 1
    elif min(x,y,z) == z and c < C-1:
        c += 1
    else:
        break
print(result)