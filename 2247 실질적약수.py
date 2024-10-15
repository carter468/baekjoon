# 실질적 약수
# Gold 5, math

n = int(input())

result = 0
for i in range(2,n//2+1):
    result = (result+i*(n//i-1))%(10**6)
print(result)