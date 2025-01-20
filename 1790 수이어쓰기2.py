# 수 이어 쓰기 2
# Gold 5, math

n,k = map(int,input().split())
k -= 1

i = 1
while True:
    x = i*(10**i-10**(i-1))
    if x <= k:
        k -= x
    else:
        a,b = divmod(k,i)
        result = 10**(i-1)+a
        break
    i += 1
    
print(str(result)[b] if n >= result else -1)