# 놀이공원

import sys
input = sys.stdin.readline

working_time = []
for _ in range(int(input())):
    s,e = map(int,input().split())
    if s%100 < 10:
        working_time.append([s-50,e+10])
    else:
        working_time.append([s-10,e+10])
working_time.sort()
longest_rest_time = 0
end = 1000
for s,e in working_time:
    if end<s:
        longest_rest_time = max(longest_rest_time,(s//100-end//100)*60+s%100-end%100)
    if e>end:
        end = e 
if end < 2200:
    longest_rest_time = max(longest_rest_time,(22-end//100)*60-end%100)
print(longest_rest_time)