# 부품 대여장
# Gold 2, 해시, 파싱

from collections import defaultdict
import sys
input = sys.stdin.readline
month_to_day = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

def change_minute(month,day,hour,minute):
    return (month_to_day[month-1]+day)*1440 + hour*60 + minute

N,l,f = input().split()
F = int(f)
L = change_minute(1,int(l[:3]),int(l[4:6]),int(l[7:9]))

rental_time = defaultdict(defaultdict)
penalty = defaultdict(int)
for _ in range(int(N)):
    data = input().strip()
    minute = change_minute(int(data[5:7]),int(data[8:10]),int(data[11:13]),int(data[14:16]))
    part,name = data[17:].split()
    if part in rental_time[name]:
        overtime = minute-rental_time[name][part]-L
        if overtime>0:
            penalty[name] += F*overtime
        del rental_time[name][part]
    else:
        rental_time[name][part] = minute

if penalty:
    for name in sorted(penalty):
        print(name,penalty[name])
else:
    print(-1)