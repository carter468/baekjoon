# 방 번호
# Gold 4, 브루트포스

n = int(input())

for a in range(1,min(87655,n//2+1)):
    b = str(n-a)
    a = str(a)
    if len(set(a+b)) == len(a)+len(b):
        print(f'{a} + {b}')
        break
else:
    print(-1)