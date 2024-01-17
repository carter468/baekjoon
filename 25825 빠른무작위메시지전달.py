# 빠른 무작위 메시지 전달
# Gold 4, backtracking, bruteforcing

def f(t,c,i):
    global result
    if c == 6:
        result = min(result,t)
        return
    if c >= result: return

    for j in range(12):
        if visited[j//2] == False:
            if j%2 == 0: k = j+1
            else: k = j-1
            visited[j//2] = True
            f(t+arr[i][j],c+1,k)
            visited[j//2] = False

arr = [tuple(map(int,input().split())) for _ in range(12)]

result = 10**5
visited = [False]*6
for i in range(12):
    visited[i//2] = True
    f(0,1,i)
    visited[i//2] = False

for i in range(6):
    result += arr[i*2][i*2+1]
print(result)