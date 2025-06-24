# 엘나스의 용사
# Gold 3, prefix sum, bruteforcing

# 포탈입구가 1로 고정될 수 있는 것을 파악한다면 더 빠른 코드로 수정 가능

N,M,K = map(int,input().split())
H = tuple(map(int,input().split()))
L = tuple(map(int,input().split()))

count = [0]*201 # 레벨 i인 용사의 숫자
for h in H: count[h] += 1

arr = []
for i,l in enumerate(L):
    arr.append((l,i+1))
arr.sort()
floor = [0]*200 # 레벨 i인 용사가 가야하는 층
for i in range(M-1):
    for j in range(arr[i][0],arr[i+1][0]):
        floor[j] = arr[i][1]
for j in range(arr[-1][0],200):
    floor[j] = arr[-1][1]

result = -1,0,0
for i in range(1,M): # 포탈입구
    for j in range(i+1,M+1): # 포탈출구
        diff = [0]*(M+1) # 목표층수를 갈때 절약하는 이동시간
        for k in range(2,M+1): # 목표층수
            d = i-1+abs(j-k)
            diff[k] = max(0,k-1-d)
        x = 0
        t = []
        for l in range(199,0,-1): # 레벨 l인 용사들이 절약한 이동시간 합 계산
            t.append(diff[floor[l]])
            x += sum(t[-K:])*count[l]
        if x > result[0]: result = x,i,j
print(result[1],result[2])
print(result[0])