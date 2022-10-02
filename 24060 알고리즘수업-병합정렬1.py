# 알고리즘 수업 - 병합 정렬 1

def merge_sort(p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(p,q)
        merge_sort(q+1,r)
        merge(p,q,r)

def merge(p,q,r):
    global cnt
    tmp = []
    i,j = p,q+1
    while i<=q and j<=r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= q:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        a[i] = tmp[t]
        i += 1
        t += 1 
        cnt += 1
        if cnt == k:
            print(a[i-1])
            quit(0)

n,k = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
merge_sort(0,n-1)
print(-1)