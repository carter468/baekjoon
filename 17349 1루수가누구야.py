# 1루수가 누구야
# Gold 4, implementation

arr = [tuple(map(int,input().split())) for _ in range(9)]

result = []
for i in range(9):
    check = [-1]*9
    for j in range(9):
        a,b = arr[j]
        b -= 1
        if j == i: a ^= 1
        if check[b] != -1 and check[b] != a: break
        check[b] = a
    else:
        if check.count(1) == 1:
            result.append(check.index(1)+1)
        elif check.count(1) == 0:
            for j in range(9):
                if check[j] == -1: result.append(j+1)

if len(set(result)) == 1: print(result[0])
else: print(-1)