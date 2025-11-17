# 순열
# Gold 1, ad hoc

input()
P = tuple(map(int,input().split()))

visited = set()
count = 0
for a in P:
    if a not in visited:
        count += 1
        while a not in visited:
            visited.add(a)
            a = P[a]

print(count if count > 1 else 0)