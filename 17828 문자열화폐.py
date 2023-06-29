# 문자열 화폐
# Gold 5, greedy

n,x = map(int,input().split())

if 26*n < x or x < n:
    print('!')
else:
    result = ['A']*n
    x -= n
    for i in range(n):
        if x >= 25:
            result[-i-1] = 'Z'
            x -= 25
        else:
            result[-i-1] = chr(x+65)
            break
    print(''.join(result))