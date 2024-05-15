# 카드 바꾸기
# Gold 5, bruteforcing, math

n = int(input())
arr = tuple(map(int,input().split()))

result = n-1
for i in range(n):
    for j in range(i+1,n):
        if (arr[i]-arr[j])%(i-j) == 0:
            d = (arr[i]-arr[j])//(i-j)
            a0 = arr[i]-d*i
            count = 0
            for k in range(n):
                if arr[k] != a0+d*k: count += 1
            result = min(result,count)
print(result)