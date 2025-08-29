# 상자 빌리기
# Platinum 5, deque trick

from collections import deque

for _ in range(int(input())):
    N,X = map(int,input().split())
    hs,ha,hb,hc = map(int,input().split())
    ws,wa,wb,wc = map(int,input().split())

    H,W = [0]*N,[0]*N
    H[0] = hs%hc+1
    W[0] = ws%wc+1
    for i in range(1,N):
        H[i] = H[i-1]+1+(H[i-1]*ha+hb)%hc
        W[i] = (W[i-1]*wa+wb)%wc+1

    answer = -1
    q = deque()
    for i in range(N):
        h,w = H[i],W[i]
        while q and h-q[0][1] > X:
            q.popleft()
        if q:
            answer = max(answer,h*w+q[0][0])
        while q and q[-1][0] < h*w:
            q.pop()
        q.append((h*w,h))
    print(answer)