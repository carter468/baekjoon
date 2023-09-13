# 리벤지 오브 피타고라스
# Gold 5, math

while n:=int(input()):
    m = n*n
    c = 0
    for i in range(1,n):
        if m%i == 0 and (i+m//i)%2 == 0 and (m//i-i)//2 > n:
            c += 1
    print(c)