# 제곱ㄴㄴ수
# Gold 1, 정수론, 에라토스테네스의 체

start,end = map(int,input().split())
seive = [True]*(end-start+1)

i = 2
while i**2<=end:
    k = i**2
    j = (start-1)//k+1
    while j*k<=end:
        seive[j*k-start] = False
        j += 1
    i += 1
print(sum(seive))