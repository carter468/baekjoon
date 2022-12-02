# 거의 소수
# Gold 5, 수학

MAX = 10**7+1

# 소수 테이블
prime = [True]*MAX
prime[1] = False
for i in range(2,int(MAX**0.5)):
    if prime[i]:
        for j in range(i*2,MAX,i):
            prime[j] = False

a,b = map(int,input().split())

# b**0.5 이하의 소수에 대해 a이상 b이하 범위 내의 거의소수 카운트
answer = 0
for i in range(2,int(b**0.5)+1):
    if prime[i]:
        for j in range(2,MAX):
            if i**j>b:
                break
            if i**j>=a:
                answer += 1
print(answer)