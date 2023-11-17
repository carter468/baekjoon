# 멍멍이 쓰다듬기
# Gold 5, math

x,y = map(int,input().split())

z = y-x
i = 0
while i*i < z:
    i += 1

if i*(i-1) >= z: print(max(0,i*2-2))
else: print(i*2-1)