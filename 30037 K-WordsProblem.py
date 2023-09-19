# K-Words Problem
# Gold 3, implementation

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().split()[::-1]
    
    result = []
    while s:
        a = s.pop()
        if a == 'Korea':
            if len(result) >= 2 and result[-1] == 'of' and result[-2][-1] not in '!?,':
                result.pop()
                b = result.pop()
                result.append('K-'+b[0].upper()+b[1:])
            else:
                count = 1
                while s[-1] == 'Korea':
                    s.pop()
                    count += 1
                b = s.pop()
                if b == 'of' and s[-1] in ('Korea','Korea!','Korea?','Korea,','Korea.'):
                    b = s.pop()
                    result.append('K-'*count+b)
                else:
                    result.append('K-'*count+b[0].upper()+b[1:])
        elif a in ('Korea!','Korea?','Korea,','Korea.'):
            if len(result) >= 2 and result[-1] == 'of' and result[-2][-1] not in '!?,':
                result.pop()
                b = result.pop()
                result.append('K-'+b[0].upper()+b[1:]+a[-1])
            else: result.append(a)
        else:
            result.append(a)

    print(*result)