# 곱셈 게임
# Gold 4, game theory

while True:
    try:
        n = int(input())
        while n > 18:
            n /= 18
        if n <= 9: print('Baekjoon wins.')
        else: print('Donghyuk wins.')
    except:
        break