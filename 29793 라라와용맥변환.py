# 라라와 용맥 변환
# Gold 3, casework, adhoc, bruteforce, greedy

n,h = map(int,input().split())
s = input()

if h >= 4:
    if n >= 4: print(-1)
    else: print(n-len(set(s)))
elif h == 3:
    result = 10**9
    for x in 'SRW','SWR','RWS','RSW','WSR','WRS':
        c = 0
        for i in range(n):
            if s[i] != x[i%3]:
                c += 1
        result = min(result,c)
    print(result)
elif h == 2:
    result = 0
    i = 1
    while i < n:
        if s[i] == s[i-1]:
            result += 1
            i += 1
        i += 1
    print(result)
else:
    print(0)