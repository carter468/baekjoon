# 절대값 힙

class minheap:
    def __init__(self):
        self.heap= [0] 
    
    # def printheap(self):
    #     print(self.heap)
        
    def check(self):        # 힙의 최소값 반환
        if len(self.heap) == 1:
            return 0
        else:
            return self.heap[1]

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

heap_p = minheap() # 입력받은 양수 최소 힙
heap_n = minheap() # 입력받은 음수를 -1를 곱한 값들의 최소 힙 
n = int(input())
for _ in range(n):
    x = int(input())
    if x==0:
        x = heap_p.check()
        y = heap_n.check()
        if x==0:        # 양수 힙이 비어있다
            print(heap_n.heappop()*-1)
        elif y==0:      # 음수 힙이 비어있다
            print(heap_p.heappop())
        else:
            if x < y: #절대값 비교후 작은 쪽 pop
                print(heap_p.heappop())
            else:           # 음수쪽이 작거나 같으면 음수쪽 pop
                print(heap_n.heappop()*-1)
    elif x>0:       # 양수는 양수힙
        heap_p.heappush(x)
    else:           # 음수는 음수힙
        heap_n.heappush(x*-1)
    # heap_p.printheap()
    # heap_n.printheap()

# print(heap.heappop())
# heap.heappush(13345)
# heap.heappush(1)
# heap.heappush(2)
# print(heap.heappop())
# print(heap.heappop())
# print(heap.heappop())
# print(heap.heappop())
# heap.heappush(32)
