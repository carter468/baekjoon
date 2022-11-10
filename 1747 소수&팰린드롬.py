# 소수&팰린드롬

n = int(input())

MAX = 1003002
prime = [True]*MAX
prime[1] = False
for i in range(2,int(MAX**0.5)+1):
    if prime[i]:
        for j in range(i*2,MAX,i):
            prime[j] = False
for i in range(n,MAX):
    if prime[i]:
        if i == int(str(i)[::-1]):
            print(i)
            break