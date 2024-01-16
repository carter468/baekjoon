# 3+1 하노이 탑
# Gold 3, ad hoc

def move(c,a,b):
    global count
    if c < 1: return
    if c == 1:
        count += 1
        result.append((M[a],M[b]))
        return
    if b == 3:
        move(c-2,a,(a+1)%3)
        move(1,a,(a+2)%3)
        move(1,a,3)
        move(1,(a+2)%3,3)
        move(c-2,(a+1)%3,3)
    else:
        move(c-1,a,3-a-b)
        move(1,a,b)
        move(c-1,3-a-b,b)

M = 'ABCD'
count = 0
result = []
move(int(input()),0,3)
print(count)
for r in result:
    print(*r)