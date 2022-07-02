# 공유기 설치

import sys
input = sys.stdin.readline

n,c = map(int,input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()   

start = 1
end = max(house)
m = min(house)

while start<=end:
    mid = (start+end)//2    

    last_house = m    #가장 왼쪽 집 설치
    cnt = 1
    for i in range(1,n):
        if house[i] - last_house >= mid:  #설치한 집 사이의 거리가 mid 보다 크거나 같아야한다.
            last_house = house[i]
            cnt += 1
    if cnt >= c:        #설치대수가 많다면 거리를 늘려야한다.
        start = mid+1
    else:
        end = mid-1

print(end)
