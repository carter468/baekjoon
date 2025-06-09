# Dreary Design (Large2)
# Gold 5, math

for t in range(int(input())):
    K,V = map(int,input().split())
    print(f'Case #{t+1}: {V*(V+1)*(3*K-2*V+2)+K+1}')