# 냅색문제

n,c = map(int,input().split())
weight = list(map(int,input().split()))

a_w,b_w = weight[:n//2],weight[n//2:]   # 두 그룹으로 나눈다
a_c,b_c = [],[]         # 각 그룹의 조합으로 만들 수 있는 무게가 들어간다

def combination(arr,comb,idx,w):    # 그룹, 조합, 인덱스, 무게
    if idx >= len(arr):
        comb.append(w)
        return
    combination(arr,comb,idx+1,w)           # 넣지않는경우
    combination(arr,comb,idx+1,w+arr[idx])  # 넣는경우

def bs(arr,target,start,end):   # 이분탐색
    while start<end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid+1
        else:
            end = mid
    return end

combination(a_w,a_c,0,0)
combination(b_w,b_c,0,0)
b_c.sort()

cnt = 0
for i in a_c:       
    if c-i < 0:
        continue
    cnt += bs(b_c,c-i,0,len(b_c))
print(cnt)