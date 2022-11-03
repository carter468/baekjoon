# 오등큰수

from collections import Counter
n = int(input())
a = list(map(int,input().split()))

count_a = Counter(a)
answer = [-1]*n
stack = []
for i in range(n):
    while stack and count_a[a[stack[-1]]] < count_a[a[i]]:
        answer[stack.pop()] = a[i]
    stack.append(i)
print(*answer)