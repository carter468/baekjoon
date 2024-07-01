# 합성인수분해
# Gold 5, greedy, number theory

n = int(input())

arr = []
for i in range(2,int(n**0.5)+1):
    while n%i == 0:
        n //= i
        arr.append(i)
if n > 1:
    arr.append(n)

if len(arr) == 1: print(-1)
else:
    result = []
    for i in range(len(arr)//2):
        result.append(arr[i*2]*arr[i*2+1])
    if len(arr)%2 == 1:
        result[-1] = result[-1]*arr[-1]
    print(*result)