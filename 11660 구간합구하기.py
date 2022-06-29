# 구간 합 구하기 5

# n, m = 4, 3
# arr = [[1, 2, 3,4, 0], [2,3,4,5, 0], [3,4,5,6, 0], [4,5,6,7, 0], [0, 0, 0, 0, 0]]
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split()))+[0])
arr.append([0]*(n+1))

for i in range(n):
    for j in range(n):
        #구간 합 = 왼쪽칸 + 위쪽칸 - 왼쪽위 대각선칸
        arr[i][j] += arr[i][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split()) 
    print(arr[x2-1][y2-1]-arr[x1-2][y2-1]-arr[x2-1][y1-2]+arr[x1-2][y1-2])
