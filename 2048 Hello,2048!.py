# Hello, 2048!
# Gold 4, number theory

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l,r = map(int,input().split())
    if r >= 4:
        print(r)
    else:
        x = ''
        for i in range(l,r+1):
            x += str(1<<i)
        x = int(x)
        count = 0
        while x%2 == 0:
            x >>= 1
            count += 1
        print(count)

# 증명
# 각 거듭제곱 수를 기준으로 숫자를 자른다면 예)81632 -> 80000+1600+32
# r >= 4일때 2^4 = 16으로 두자리수이기 때문에 
# 2^(r-k)에 대한 숫자는 뒤에 0이 적어도 k+1개 있다.
# 그러므로 k >= 1 에 대해 2^(r-k)*10^(k+1) 는 2^(r+1)의 배수이다.
# 따라서 l부터 r-1까지 잘라진 숫자를 2^r로 나누면 모두 짝수여야하고 r번째는 1이여야 하므로
# 모두 더하면 홀수가 되고 더이상 2로 나눌 수 없다.