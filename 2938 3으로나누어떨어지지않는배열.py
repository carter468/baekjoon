# 3으로 나누어 떨어지지 않는 배열
# Gold 5, constructive, case work

input()
arr = [[] for _ in range(3)]
for x in map(int,input().split()):
    arr[x%3].append(x)

a,b,c = map(len,arr)
result = []
if a == 0:
    if b > 0 and c > 0:
        print(-1)
    else:
        result.extend(arr[1])
        result.extend(arr[2])
        print(*result)
elif a == 1:
    result.extend(arr[1])
    result.extend(arr[0])
    result.extend(arr[2])
    print(*result)
elif b+c < a-1:
    print(-1)
else:
    t = 1 if b else 2
    for i in range(a-1):
        result.append(arr[0][i])
        result.append(arr[t].pop())
        if not arr[t]: t += 1
    if t < 3 and arr[t]:
        result.extend(arr[t])
    result.append(arr[0][-1])
    if t == 1:
        result.extend(arr[2])
    print(*result)