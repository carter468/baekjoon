# 이항 계수 3

#페르마의 소정리에 의하면 (a**-1)%p = (a**(p-2))%p
#nCk %p = n!/((n-k)!k!) %p = (n! %p * ((n-k)!k!)**(p-2) %p) %p

def facmod(n):   # n! mod p
    global p
    ans = 1
    for i in range(2,n+1):
        ans = (ans*i)%p
    return ans

def powmod(expo):   #(k!(n-k)!)**(p-2) 분할정복
    global p,knk
    if expo==1:
        return knk%p
    elif expo==2:
        return (knk**2)%p
    else:
        if expo%2 == 0:
            return (powmod(expo//2)**2) % p
        else:
            return ((powmod((expo-1)//2))**2)*knk % p

n,k = map(int,input().split())      
p = 1000000007  #p는 소수
knk = (facmod(k)*facmod(n-k))

print((facmod(n)*powmod(p-2)) % p)
