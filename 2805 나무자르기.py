# 나무자르기

n,m = 4,7
trees = [20,15,10,17]
n,m = 5,20
trees = [4,42,40,26,46]
n,m = map(int,input().split())
trees = list(map(int,input().split()))

start = 0
end = max(trees)

while start<=end:
    mid = (start+end)//2
    result = 0
    for x in trees:
        if mid<x:           #나무가 더 높으면 자른다
            result += x-mid

    if result<m:            #목표길이보다 짧으면 
        end = mid-1         #절단기를 내린다
    else:
        start = mid+1       

print(end)
    
