# 페르마의 크리스마스 정리

import sys

MAX_NUMBER = 1000000
prime = [True]*MAX_NUMBER
prime_count = [0]*MAX_NUMBER        # 소수누적합
count = 0
prime_count_ferma = [0]*MAX_NUMBER  # 제곱수의합소수 누적합
count_ferma = 1                     # 2는 mod4=1 이 아니므로 예외적으로 처리
for i in range(2,MAX_NUMBER):
    if prime[i] == True:
        count += 1
        prime_count[i] = count
        if i%4 == 1:
            count_ferma += 1
            prime_count_ferma[i] = count_ferma
        else:
            prime_count_ferma[i] = count_ferma
        for j in range(i*2,MAX_NUMBER,i):
            prime[j] = False
    else:
        prime_count[i] = count
        prime_count_ferma[i] = count_ferma

while True:
    l,u = map(int,sys.stdin.readline().split())
    if l==-1 and u==-1:
        break
    start = l if l>0 else 1
    end = u if u>0 else 1
    x = prime_count[end]-prime_count[start-1]
    y = prime_count_ferma[end]-prime_count_ferma[start-1]
    print(l,u,x,y)