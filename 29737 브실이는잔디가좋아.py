# 브실이는 잔디가 좋아
# Gold 4, implementation

n,w = map(int,input().split())
result = []
for _ in range(n):
    name = input()
    s = 0   # 스트릭길이(조건1)
    d = 0   # 스트릭내 프리즈개수(조건2)
    c = 0   # 시작날짜(조건3)
    e = 0   # 실패한날(조건4)
    r = []  # 스트릭 정보
    f = 0   # 스트릭 꼬리에 붙은 프리즈개수
    arr = [input() for _ in range(7)]
    for i in range(w):
        for j in range(7):
            k = arr[j][i]
            if k == 'O':
                if s == 0: c = 7*i+j
                s += 1
                f = 0
            elif k == 'F':
                if s > 0:
                    d += 1
                    f += 1
            elif k == 'X':
                e += 1
                if s > 0: r.append([-s,d-f,c])
                s,d,f = 0,0,0
    if s > 0: r.append([-s,d-f,c])
    if r:
        result.append(sorted(r)[0]+[e,name])
    else:
        result.append([0,0,0,e,name])
result.sort()

rank = 1
print(f'{rank}. {result[0][4]}')
for i in range(1,n):
    if result[i][:4] != result[i-1][:4]: rank += 1
    print(f'{rank}. {result[i][4]}')