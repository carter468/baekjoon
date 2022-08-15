# 킹 퀸 룩 비숍 나이트 폰

chess = [1,1,2,2,2,8]
white = list(map(int,input().split()))

for i in range(6):
    print(chess[i]-white[i],end=' ')