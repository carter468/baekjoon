# MOO 게임

n = int(input())
s = [3]
i = 1
while True:
    s.append(s[-1]*2+i+3)
    if s[-1] > n:
        break
    i += 1

i = len(s)-1
while True:
    if i==0:
        print('moo'[n-1])
        break
    if s[i-1] < n <= s[i]-s[i-1]:
        if n-s[i-1] == 1:
            print('m')
            break
        else:
            print('o')
            break
    if n > s[i]-s[i-1]:
        n -= s[i]-s[i-1]
    i -= 1