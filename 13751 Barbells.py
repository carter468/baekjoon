# Barbells
# Gold 4, backtracking

def solve(idx,left,right):
    if left == right: result.add(left*2)
    if idx == p: return
    solve(idx+1,left+plates[idx],right)
    solve(idx+1,left,right+plates[idx])
    solve(idx+1,left,right)

b,p = map(int,input().split())
bars = [int(input()) for _ in range(b)]
plates = [int(input()) for _ in range(p)]

result = set()
solve(0,0,0)

answer = set()
for bar in bars:
    for r in result:
        answer.add(bar+r)

for a in sorted(answer):
    print(a)