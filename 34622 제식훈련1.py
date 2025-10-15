# 제식 훈련 1
# Gold 2, ad hoc, constructive, case work

N,M,D,E,X,Y = map(int,input().split())

print(3)
if X <= 0 and Y <= 0:
    print(2,1,D-X)
    print(1,2,D-X-Y)
    print(1,1,E)
elif X <= 0:
    print(2,1,D-X)
    print(1,1,Y+E)
    print(1,2,E)
elif Y <= 0:
    print(1,2,D-Y)
    print(1,1,X+E)
    print(2,1,E)
else:
    print(1,1,X+E)
    print(2,1,Y+E)
    print(2,2,E)