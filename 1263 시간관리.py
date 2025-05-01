# 시간 관리
# Gold 5, greedy

x = 10**6
for t,s in sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:-x[1]):
    x = min(x,s)-t
print(-1 if x < 0 else x)