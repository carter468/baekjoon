# 잘못 작성한 요세푸스 코드
# Platinum 4, math

n,k = map(int,input().split())

result = 0
if n > k:
    result += (n-k)*k
    n = k

i = 2
while i*i <= k:
    l = k//i+1
    if n >= l:
        c = n-l+1
        result += k*c-(l+n)*c//2*(i-1)
        n = l-1
    i += 1

for i in range(1,n+1):
    result += k%i
print(result)