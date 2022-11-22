# SSR
# Gold 3, 정수론

n,m = map(int,input().split())
answer = 0
for i in range(1,n+1):
    # 두 수의 곱이 제곱수가 되는 쌍을 찾는다
    for j in range(int(i**0.5),1,-1):
        # i가 제곱수의 배수이면 그 제곱수로 나눠준다
        if i%(j**2)==0:
            i //= j**2
    # i*제곱수의 형식으로 곱해주면 제곱수가 된다
    answer += int((m/i)**0.5)
print(answer)