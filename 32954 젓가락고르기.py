# 젓가락 고르기
# Gold 4, greedy, ad hoc

N,K = map(int,input().split())
A = sorted(map(int,input().split()))

pair = 0
for a in A:
    pair += a//2
if K == 0: print(0)
elif pair < K: print(-1)
else:
    remain = K
    count = N
    for a in A:
        c = (a-1)//2
        if c < remain:
            count += c*2
            remain -= c
        else:
            count += remain*2-1
            remain = 0
            break
    print(count+remain)