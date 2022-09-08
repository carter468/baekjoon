# 날짜 계산

e,s,m = map(int,input().split())

k = 0
while True:
    k += 1
    if k%15 == e%15 and k%28 == s%28 and k%19 == m%19:
        break
print(k)