# 일이 커졌어
# Gold 5, greedy

n = int(input())

a = n//2+1
b = a-1
for i in range(n):
    if i%2 == 0:
        print(a,end=' ')
        a += 1
    else:
        print(b,end=' ')
        b -= 1
