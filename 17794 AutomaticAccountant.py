# Automatic Accountant
# Platinum 4, segtree

# 세그먼트트리에 질량제한이 i~j인 구간을 가진 슬롯의 최소 인덱스를 저장
# 슬롯은 구멍크기 내림차순 정렬을 하고
# 코인을 구멍크기 내림차순으로 탐색하면서
# a가 현재 구멍크기 u보다 큰 슬롯을 세그먼트트리에 업데이트한 후
# 질량제한 1~v까지 구간의 최소 인덱스가 구하는 길이가 된다.

M = 10**5+1

def query(start,end,node,left,right):
    if left > end or right < start:
        return M
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return min(query(start,mid,node*2,left,right),query(mid+1,end,node*2+1,left,right))

def update(start,end,node,idx,v):
    if idx < start or idx > end:
        return
    tree[node] = min(tree[node],v)
    if start == end:
        return
    mid = (start+end)//2
    update(start,mid,node*2,idx,v)
    update(mid+1,end,node*2+1,idx,v)

slot = []
for i in range(int(input())):
    a,b = map(int,input().split())
    slot.append((a,b,i+1))
slot.sort()
coin = sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:-x[0])

tree = [M]*(M*4)
result = 0
for u,v in coin:
    while slot and slot[-1][0] >= u:
        a,b,i = slot.pop()
        update(1,M-1,1,b,i)
    result += query(1,M-1,1,1,v)
print(result)