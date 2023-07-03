# 같은 나머지
# Gold 5, 수학

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

n = int(input())
arr = tuple(map(int,input().split()))

result = arr[0]-arr[-1]
for i in range(n-1):
    result = gcd(result,arr[i]-arr[i+1])

print(abs(result))