# 최대 힙

import sys
input = sys.stdin.readline

def heapify_add(x):
    heap.append(x)
    idx = len(heap)-1
    while idx > 1:  # 위방향으로 탐색
        if heap[idx] > heap[idx//2]:
            heap[idx],heap[idx//2] = heap[idx//2],heap[idx]
            idx //= 2
        else:
            return

def heapify_remove():
    heap[1] = heap[-1]
    heap.pop()
    l = len(heap)-1     # 마지막 idx = heap길이-1
    idx = 1             # 부모노드idx
    while idx<=l//2:    # 아래방향으로 탐색
        if idx*2 == l:  # 자녀노드가 하나인경우
            if heap[idx] < heap[idx*2]:
                heap[idx],heap[idx*2] = heap[idx*2],heap[idx]
            return
        else:           #자녀노드가 두개인경우
            if heap[idx] >= max(heap[idx*2],heap[idx*2+1]):
                return
            if heap[idx*2] > heap[idx*2+1]:
                if heap[idx*2] > heap[idx]:
                    heap[idx*2], heap[idx] = heap[idx], heap[idx*2]
                    idx = idx*2
            else:
                if heap[idx*2+1] > heap[idx]:
                    heap[idx*2+1], heap[idx] = heap[idx], heap[idx*2+1]
                    idx = idx*2+1

heap = [0]     

n = int(input())
for _ in range(n):
    x = int(input())
    if x==0:
        if len(heap) == 1:
            print(0)
        else:
            print(heap[1])
            heapify_remove()
    else:
        heapify_add(x)