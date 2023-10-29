# 장난꾸러기 영훈
# Gold 5, math

pw = list(input())
k = int(input())-1

for i in range(len(pw)):
    if pw[i] == '6': pw[i] = '1'
    elif pw[i] == '7': pw[i] = '2'

idx = len(pw)-1
while k:
    while idx >= 0 and pw[idx] not in ('1','2'):
        idx -= 1
    if idx == -1:
        print(-1)
        break
    if k%2 == 1:
        if pw[idx] == '1': pw[idx] = '6'
        elif pw[idx] == '2': pw[idx] = '7'
    k //= 2
    idx -= 1
else: print(''.join(pw))