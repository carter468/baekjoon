# 최소 힙

class minheap:
    def __init__(self):
        self.heap = [0]
    
    def get_min_child(self,idx):    # 자녀중 작은 쪽의 index , 자녀가 없다면 -1 을 return
        if len(self.heap)-1 >= idx*2+1:
            if self.heap[idx * 2] < self.heap[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1
        elif len(self.heap)-1 == idx*2:
            return idx * 2
        else:
            return -1

    def heappush(self,x):
        self.heap.append(x)
        idx = len(self.heap) - 1
        while idx>1:    # 위로 올라가며 힙 완성
            if self.heap[idx] < self.heap[idx//2]:
                self.heap[idx],self.heap[idx//2] = self.heap[idx//2],self.heap[idx]
            else:
                return
            idx //= 2
        
    def heappop(self):
        if len(self.heap) == 1:
            return 0
        else:
            root_value = self.heap[1]       #최소값
            self.heap[1] = self.heap[-1]    #마지막값을 root로 이동
            self.heap.pop()
            idx = 1
            l = len(self.heap) - 1
            while idx <= l//2:             #아래로 내려가며 힙 완성
                child = self.get_min_child(idx)
                if child == -1:
                    break
                elif self.heap[idx] > self.heap[child]:
                    self.heap[idx],self.heap[child] = self.heap[child],self.heap[idx]
                else:
                    break
                idx = child
            return root_value

import sys
input = sys.stdin.readline

heap = minheap()
n = int(input())
for _ in range(n):
    x = int(input())
    if x==0:
        print(heap.heappop())
    else:
        heap.heappush(x)

# print(heap.heappop())
# heap.heappush(13345)
# heap.heappush(1)
# heap.heappush(2)
# print(heap.heappop())
# print(heap.heappop())
# print(heap.heappop())
# print(heap.heappop())
# heap.heappush(32)
