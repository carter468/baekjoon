# Huge Numbers
# Gold 5, exponentiation by squaring

for t in range(int(input())):
    A,N,P = map(int,input().split())
    answer = A
    for i in range(1,N+1):
        answer = pow(answer,i,P)
    print(f'Case #{t+1}: {answer}')