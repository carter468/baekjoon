# 푸앙이와 러닝머신
# Gold 5, 많은 조건 분기, 그리디 알고리즘

x,t = map(int,input().split())  # 목표거리, 제한시간

if x<=t:    # 1
    print(1)
    print(t-x,1)
elif x<=4*t and x%4==0:    # 4
    print(1)
    print(t-x//4,4)
elif t-x//4>=x%4:    # 1,4
    print(2)
    print(t-x//4-x%4,4)
    print(t-x%4,1)
elif x<=8*t:    # 1,4,8
    if x%8==0:  # 8
        print(1)
        print(t-x//8,8)
    else:
        a = x%8 # 남은 거리(0~7)
        b = t-x//8  # 남은 시간
        if a<=b:    # 1,8
            print(2)
            print(b-a,8)
            print(t-a,1)
        elif a==4 and b>=1: # 4,8
            print(2)
            print(b-1,8)
            print(t-1,4)
        elif a>4 and a-4<=b-1:  # 1,4,8
            print(3)
            print(b-a+3,8)
            print(t-a+3,4)
            print(t-a+4,1)
        else:
            print(-1)
else:
    print(-1)