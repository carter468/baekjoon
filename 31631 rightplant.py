# :rightplant:
# Gold 3, ad hoc, constructive

n = int(input())

arr = [True]*(n+1)
result = []
i = n-1
while i > 0:
    result.append(i)
    arr[i] = False
    if i > 1:
        result.append(i-1)
        arr[i-1] = False
    i -= 4
for i in range(1,n+1):
    if arr[i]: result.append(i)
print(*result)