# 나3곱2
# Gold 5, constructive

input()
arr = list(map(int,input().split()))

a = arr[0]
res1,res2 = [a],[]
arr = set(arr)
arr.remove(a)
if a%3 != 0:
    while a*2 in arr:
        res1.append(a*2)
        arr.remove(a*2)
        a *= 2
else:
    while a*2 in arr or a//3 in arr:
        if a*2 in arr:
            res1.append(a*2)
            arr.remove(a*2)
            a *= 2
        else:
            res1.append(a//3)
            arr.remove(a//3)
            a //= 3
a = res1[0]
while a//2 in arr or a*3 in arr:
    if a//2 in arr:
        res2.append(a//2)
        arr.remove(a//2)
        a //= 2
    else:
        res2.append(a*3)
        arr.remove(a*3)
        a *= 3

print(*(res2[::-1]+res1))