# 최고의 초콜릿 성지순례
# Gold 1, DP, greedy, case work

for _ in range(int(input())):
    n = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(2)]
    a,b,c,d = map(int,input().split())
    if (a,b) > (c,d): a,b,c,d = c,d,a,b
    a,b,c,d = a-1,b-1,c-1,d-1

    if a == c: x = 0
    else: x = arr[b-1][a]
    m1 = max(0,x)
    for i in range(a-1,-1,-1):
        m1 = max(m1,x+arr[b][i],x+arr[b-1][i])
        x += arr[b][i]+arr[b-1][i]
        m1 = max(m1,x)
    if a == c: x = 0
    else: x = arr[d-1][c]
    m2 = max(0,x)
    for i in range(c+1,n):
        m2 = max(m2,x+arr[d][i],x+arr[d-1][i])
        x += arr[d][i]+arr[d-1][i]
        m2 = max(m2,x)
    result = m1+m2+arr[b][a]+arr[d][c]
    for i in range(a+1,c):
        if min(arr[0][i],arr[1][i]) > 0: result += arr[0][i]+arr[1][i]
        else: result += max(arr[0][i],arr[1][i])
    if a == c: result = max(m1,m2)+arr[b][a]+arr[d][c]
    print(result)