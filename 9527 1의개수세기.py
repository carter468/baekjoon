# 1의 개수 세기
# Gold 2, math

def count(n):
    n = bin(n)[2:]
    l = len(n)-1
    result = int(n[-1])
    for i in range(l):
        if n[i] == '1':
            result += (1<<(l-i-1))*(l-i)+1
            for j in range(l-i):
                if n[-1-j] == '1':
                    result += 1<<j
    return result

a,b = map(int,input().split())
print(count(b)-count(a-1))