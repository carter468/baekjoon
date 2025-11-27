# 배열 점수 최대화
# Gold 4, greedy, bruteforcing, math

N,K = map(int,input().split())

result = 0
for i in range(N+1): # 증가시킨 횟수
    j = N-i # 배열의 길이
    x = K+i # 가장 큰 수
    y = x+(1-j)//2 # 중앙값
    result = max(result,j*y)
print(result)