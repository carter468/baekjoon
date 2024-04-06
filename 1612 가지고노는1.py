# 가지고 노는 1
# Gold 5, number theory

n = int(input())

if n%2 == 0 or n%5 == 0: print(-1)
else:
    a = 1
    i = 1
    while True:
        if a%n == 0:
            print(i)
            break
        a = (a*10+1)%n
        i += 1