# 랜선 자르기

# 처음 푼 코드
# import sys
# input = sys.stdin.readline
# def cut(n): # 길이 n으로 잘랐을 때 개수
#     cnt = 0
#     for i in range(len(lan_cable)):
#         cnt += (lan_cable[i] // n)
#     return cnt

# def find(start,end):    #start ~ end구간 이분탐색
#     global k,longest
#     if start == end-1: #구간 간격이 1인경우 start또는 end가 정답이므로
#         if cut(end) == k:
#             longest = end
#         else:
#             longest = start
#         return 
#     mid = (start+end)//2    #중간길이
#     mid_cnt = cut(mid)      #중간길이로 잘랐을때 개수
#     if mid_cnt < k:         # 적게 잘랐을때 
#         if cut(start) < k:  # 시작점으로 잘라도 개수가 모자라다 = 범위 지정이 적절하지 않다
#             find(start//2,start)   
#         else:
#             find(start,mid) # 범위 지정이 적절하다면 중간길이보다 긴 범위 제거                 
#     elif mid_cnt >= k:       # 목표 개수 이상으로 잘랐을때 
#         longest = max(longest,mid)
#         find(mid,end)       # 긴범위탐색
#     return
    
# n,k = map(int,input().split())
# lan_cable = [0]*n
# for i in range(n):
#     lan_cable[i] = int(input())
# end = min(lan_cable)  
# start = end//2
# longest = 0     # k개를 만들수있는 최대길이

# find(start,end)
# print(longest)

# 반복문을 이용해 다시 푼 코드

import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lan_cable = [0]*k
for i in range(k):
    lan_cable[i] = int(input())

start = 1
end = max(lan_cable)
while start<=end:   
    mid = (start+end)//2    #중간 위치
    cnt = 0
    for i in range(k):
        cnt += lan_cable[i]//mid    # 만들어진 선 개수
    
    if cnt >= n:        # n개 이상 만들어졌다면 
        start = mid+1   # 오른쪽 범위 탐색
    else:               # n개 보다 적게 만들어졌다면
        end = mid-1     # 왼쪽 범위 탐색
    
print(end)