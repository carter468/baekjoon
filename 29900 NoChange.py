# No Change
# Gold 4, greedy

input()

t = 0
for a in sorted(map(int,input().split()))+[10**9]:
    if t+1 < a:
        print(t+1)
        break
    t += a