# 포스택
# Gold 5, greedy

input()
arr = [0,0,0,0]
for x in map(int,input().split()):
    for i in range(4):
        if arr[-1-i] < x:
            arr[-1-i] = x
            break
    else:
        print('NO')
        break
    arr.sort()
else: print('YES')