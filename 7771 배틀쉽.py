# 배틀쉽
# Gold 5, constructive

arr = [input().split() for _ in range(10)]
for i in range(10):
    for j in range(10):
        if arr[i][j] == '100':
            x,y = i,j

result = [['.']*10 for _ in range(10)]
for i,j in (x,y),(x,y-2),(x,y-4),(x,y-6),(x-2,0),(x-2,1),(x-2,3),(x-2,4),(x-2,6),(x-2,7),(x-4,0),(x-4,1),(x-4,2),(x-4,4),(x-4,5),(x-4,6),(x-6,0),(x-6,1),(x-6,2),(x-6,3):
    result[i][j] = '#'

for r in result:
    print(''.join(r))