# 크게 만들기
# Gold 3, greedy, stack

n,k = map(int,input().split())
s = input()

count = 0
result = []
for i in range(n):
    while result and s[i] > result[-1] and count < k:
        result.pop()
        count += 1
    result.append(s[i])
        
print(''.join(result[:n-k]))