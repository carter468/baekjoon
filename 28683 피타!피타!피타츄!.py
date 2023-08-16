# 피타! 피타! 피타츄!
# Gold 5, math

def check(x):
    return True if int(x**0.5)**2 == x else False

n = int(input())
if check(n): print(-1)
else:
    result = 0
    for i in range(1,int((n/2)**0.5)+1):
        k = n-i*i
        if k > 0 and check(k): 
            result += 1
    for i in range(1,int(n**0.5)+1):
        if n%i == 0 and (i+n//i)%2 == 0: 
            result += 1
    print(result)