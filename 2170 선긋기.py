# 선 긋기

import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n):
    line.append(tuple(map(int,input().split())))
line.sort()
start = line[0][0]
end = line[0][1]
ans = end - start
for left,right in line:
    if right <= end:    # 이미 그은 선에 전부 겹쳐진다
        continue
    elif left < end < right:   # 일부 겹친다
        ans += right - end
        end = right
    else:   # end <= left       # 겹치지않는다
        ans += right-left
        start,end = left,right
print(ans)