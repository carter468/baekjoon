# Matching Numbers
# Gold 2, ad hoc, constructive

for _ in range(int(input())):
    N = int(input())
    if N%2 == 0:
        print('No')
        continue

    print('Yes')
    x = 1
    a = (N*3+3)//2
    for i in range(N):
        print(x,a-x)
        x += 2
        a += 1
        if x > N: x = 2