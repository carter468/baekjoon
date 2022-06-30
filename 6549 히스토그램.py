# 히스토그램에서 가장 큰 직사각형

# stack을 이용한 풀이
# while True:
#     heights = list(map(int,input().split()))
#     n = heights[0]
#     if (n==0):
#         break

#     heights[0] = 0
#     heights.append(0)
#     idx = [0]
#     ans = 0

#     for i in range(1,n+2):
#         while (idx and (heights[idx[-1]]>heights[i])):
#             pop_height = idx.pop()
#             ans = max(ans,(i-1-idx[-1])*heights[pop_height])
#         idx.append(i)
#     print(ans)

# 분할 정복을 이용한 풀이
import sys,math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def make_seg(arr,tree,node,start,end):
    if start == end:
        tree[node-1] = start        #부모노드
    else:
        mid = (start+end) // 2
        make_seg(arr,tree,node*2,start,mid)     #왼쪽자식
        make_seg(arr,tree,node*2+1,mid+1,end)   #오른쪽자식

        if arr[tree[node*2-1]] < arr[tree[node*2]]: # 작은 자식을 부모노드에 입력
            tree[node-1] = tree[node*2-1]
        else:
            tree[node-1] = tree[node*2]

def find_min_value(arr,tree,node,start,end,x,y):
    if x>end or y<start:    # 범위 초과
        return -1
    if start>=x and end<=y:
        return tree[node-1]

    mid = (start+end)//2
    left = find_min_value(arr,tree,node*2,start,mid,x,y)
    right = find_min_value(arr,tree,node*2+1,mid+1,end,x,y)

    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        if arr[left] > arr[right]:
            return right
        else:
            return left

def find_min_idx(start,end):
    idx = find_min_value(arr,tree,1,0,len(arr)-1,start,end)

    if start == end:
        return arr[idx]
    area1,area2,area3 = arr[idx]*(end-start+1),0,0

    if idx-1 >= start:
        area2 = find_min_idx(start,idx-1)
    if idx+1 <= end:
        area3 = find_min_idx(idx+1,end)

    return max(area1,area2,area3)

while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    
    n = arr[0]
    arr.pop(0)
    tree = [0] * (pow(2,math.ceil(math.log(len(arr),2))+1)-1)

    make_seg(arr,tree,1,0,len(arr)-1)
    print(find_min_idx(0,len(arr)-1))
