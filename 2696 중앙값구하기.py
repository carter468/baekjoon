# 중앙값 구하기
# Gold 2, 우선순위 큐

import sys
input = sys.stdin.readline
from heapq import heappush,heappop

for _ in range(int(input())):
    m = int(input())
    print((m+1)//2)
    array = []
    for i in range(m//10+1):
        array.append(list(map(int,input().split())))

    maxheap = []    # 중앙값 이하 최대힙
    minheap = []    # 중앙값 이상 최소힙
    count = 0
    for i in array:
        for x in i:

            # 첫 입력 => maxheap
            if not maxheap and not minheap:
                heappush(maxheap,-x)
                print(-maxheap[0],end=' ')
                count += 1

            # maxheap의 원소가 많고 중앙값보다 더 작은수가 들어오면 중앙값 교체
            elif len(maxheap) > len(minheap):
                if x < -maxheap[0]:
                    heappush(minheap,-heappop(maxheap))
                    heappush(maxheap,-x)
                else:
                    heappush(minheap,x)

            # 둘의 길이가 같고 중앙값보다 더 큰수가 들어오면 중앙값 교체
            elif len(maxheap) == len(minheap):
                if x > -maxheap[0]:
                    heappush(minheap,x)
                    heappush(maxheap,-heappop(minheap))
                else:
                    heappush(maxheap,-x)
                print(-maxheap[0],end=' ')
                count += 1
                if count%10==0:
                    print()
    print()