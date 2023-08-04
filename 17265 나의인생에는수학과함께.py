# 나의 인생에는 수학과 함께
# Gold 5, bruteforce

n = int(input())
arr = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            arr[i][j] = int(arr[i][j])

max_arr = [[-625]*n for _ in range(n)]
min_arr = [[3125]*n for _ in range(n)]
max_arr[0][0],min_arr[0][0] = arr[0][0],arr[0][0]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            if i+2 < n:
                if arr[i+1][j] == '+':
                    k = max_arr[i][j]+arr[i+2][j]
                    l = min_arr[i][j]+arr[i+2][j]
                elif arr[i+1][j] == '-':
                    k = max_arr[i][j]-arr[i+2][j]
                    l = min_arr[i][j]-arr[i+2][j]
                else:
                    k = max_arr[i][j]*arr[i+2][j]
                    l = min_arr[i][j]*arr[i+2][j]
                max_arr[i+2][j] = max(max_arr[i+2][j],k)
                min_arr[i+2][j] = min(min_arr[i+2][j],l)
            if j+2 < n:
                if arr[i][j+1] == '+':
                    k = max_arr[i][j]+arr[i][j+2]
                    l = min_arr[i][j]+arr[i][j+2]
                elif arr[i][j+1] == '-':
                    k = max_arr[i][j]-arr[i][j+2]
                    l = min_arr[i][j]-arr[i][j+2]
                else:
                    k = max_arr[i][j]*arr[i][j+2]
                    l = min_arr[i][j]*arr[i][j+2]
                max_arr[i][j+2] = max(max_arr[i][j+2],k)
                min_arr[i][j+2] = min(min_arr[i][j+2],l)
            if i+1 < n and j+1 < n:
                if arr[i][j+1] == '+':
                    k = max_arr[i][j]+arr[i+1][j+1]
                    l = min_arr[i][j]+arr[i+1][j+1]
                elif arr[i][j+1] == '-':
                    k = max_arr[i][j]-arr[i+1][j+1]
                    l = min_arr[i][j]-arr[i+1][j+1]
                else:
                    k = max_arr[i][j]*arr[i+1][j+1]
                    l = min_arr[i][j]*arr[i+1][j+1]
                if arr[i+1][j] == '+':
                    k = max(k,max_arr[i][j]+arr[i+1][j+1])
                    l = min(l,min_arr[i][j]+arr[i+1][j+1])
                elif arr[i+1][j] == '-':
                    k = max(k,max_arr[i][j]-arr[i+1][j+1])
                    l = min(l,min_arr[i][j]-arr[i+1][j+1])
                else:
                    k = max(k,max_arr[i][j]*arr[i+1][j+1])
                    l = min(l,min_arr[i][j]*arr[i+1][j+1])
                max_arr[i+1][j+1] = max(max_arr[i+1][j+1],k)
                min_arr[i+1][j+1] = min(min_arr[i+1][j+1],l)

print(max_arr[-1][-1],min_arr[-1][-1])