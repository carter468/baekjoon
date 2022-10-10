# 수상 택시

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
back = []
for _ in range(n):
    ride,dest = map(int,input().split())
    if dest < ride:
        back.append((dest,ride))
back.sort()
# start,end = back[0]
# ans = end-start
# for left,right in back:
#     if right <= end:    
#         continue
#     elif left < end < right:   
#         ans += right - end
#         end = right
#     else:   
#         ans += right-left
#         start,end = left,right
# print(m+ans*2)

start,end = back[0]
ans = 0
for left,right in back:
    if end > left:              # 겹치는 경우
        end = max(end,right)
    else:                       # 겹치지않는 경우
        ans += end - start
        start,end = left,right
ans += end - start
print(m+ans*2)

