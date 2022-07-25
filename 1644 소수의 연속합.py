# 소수의 연속 합

n = int(input())

arr = [0,0]+[1]*(n-1)
prime = []
# 에라토스테네스의 체
for i in range(2,int(n**0.5)+1):
    if arr[i] == 1:
        for j in range(i*2,n+1,i):
            arr[j] = 0
for i in range(2,n+1):
    if arr[i] == 1:
        prime.append(i)

start,end = 0,0           # 부분수열의 시작과 끝
cnt = 0                 # 경우의 수
s = 0                   # 부분합

while True:
    if s == n:       # 부분합이 N 이면 카운팅
        cnt += 1
    if s > n:
        s -= prime[start]
        start += 1
    elif end == len(prime):
        break
    else:
        s += prime[end]
        end += 1

print(cnt)