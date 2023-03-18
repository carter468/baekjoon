# 이진 트리
# Gold 3, DP_tree

k = int(input())
w = [0, 0]+list(map(int,input().split()))

result = sum(w)
for i in range(k, 0, -1):
    for j in range(1 << i, 1 << i + 1, 2):
        result += abs(w[j] - w[j + 1])
        w[j // 2] += max(w[j], w[j + 1])

print(result)