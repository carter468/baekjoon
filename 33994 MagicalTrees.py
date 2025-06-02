# Magical Trees
# Gold 3, constructive, ad hoc

N = int(input())
if N%2 == 0: print('No')
else:
    print('Yes')

    # tree 1
    for i in range(1,N):
        print(i,i+1)

    # tree 2
    print(1,2)
    print(1,N)
    if N != 3: print(N-1,N)
    for i in range(3,N,2):
        print(i,N)
        if i != 3: print(i-1,i)

    # tree 3
    print(1,N)
    print(2,3)
    for i in range(3,N,2):
        print(i,N)
        print(i,i+1)