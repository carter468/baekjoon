# 신을 모시는 사당
# Gold 5, prefix sum

input()

result = 0
x,y = 0,0
for a in input().split():
    if a == '1':
        x += 1
        y -= 1
    else:
        x -= 1
        y += 1
    result = max(result,x,y)
    x = max(0,x)
    y = max(0,y)
print(result)