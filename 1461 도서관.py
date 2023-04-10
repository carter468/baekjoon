# 도서관
# Gold 5, 그리디

n,m = map(int,input().split())
arr = sorted(map(int,input().split()))

result = -max(abs(arr[0]),abs(arr[-1]))
i = 0
while i < n and arr[i] < 0:
    result -= arr[i]*2
    i += m
i = n-1
while i >= 0 and arr[i] > 0:
    result += arr[i]*2
    i -= m

print(result)