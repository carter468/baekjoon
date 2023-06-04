# 카드 게임
# Gold 1, 게임 이론

input()

a = [1]*100001
r = 0
for x in map(int,input().split()):
    a[x] *= -1
    r += a[x]

print('koosaga' if r else 'cubelover')