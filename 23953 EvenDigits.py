# Even Digits
# Gold 4, greedy

for tc in range(int(input())):
    N = input()

    for i in range(len(N)):
        if N[i] in '13579':
            s = N[i:]
            break
    else:
        print(f'Case #{tc+1}: 0')
        continue

    l = len(s)-1
    s = int(s)
    result = 10**20
    for a in '02468':
        x = int(a+'0'*l)
        y = int(a+'8'*l)
        result = min(result,abs(s-x),abs(s-y))
    print(f'Case #{tc+1}: {result}')