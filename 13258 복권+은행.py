# 복권 + 은행
# Gold 5, math

input()
arr = tuple(map(int,input().split()))
j,c = int(input()),int(input())

result,a = arr[0],sum(arr)
for _ in range(c):
    result += j*result/a
    a += j
print(result)