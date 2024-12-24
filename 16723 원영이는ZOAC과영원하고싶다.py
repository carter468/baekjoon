# 원영이는 ZOAC과 영원하고 싶다
# Gold 5, math

N = int(input())*2

a = 2
b = N//a
answer = 0
while a <= N:
    na = a<<1
    nb = N//na
    answer += a*(b-nb)
    b = nb
    a = na
print(answer)