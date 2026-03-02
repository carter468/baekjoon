# 잘 정의된 들여쓰기
# Gold 4, stack

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    A = tuple(map(int,input().split()))

    stack = [0]
    for a in A:
        if a == 1:
            stack.append(1)
        else:
            while stack and stack[-1]+1 != a:
                stack.pop()
            if stack and stack[-1]+1 == a:
                stack[-1] += 1
            else:
                print('NO')
                break
    else:
        print('YES')