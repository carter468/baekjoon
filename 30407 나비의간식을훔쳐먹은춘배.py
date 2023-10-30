# 나비의 간식을 훔쳐먹은 춘배
# Gold 4, bruteforcing

n = int(input())
h,d,k = map(int,input().split())
damage = [int(input()) for _ in range(n)]

result = -1
q = [(h,0,d,1)]
while q:
    hp,i,dist,ult = q.pop()
    if hp <= 0: continue
    if i == n: 
        result = max(result,hp)
        continue
    if ult == 2:
        dmg = 0
        ult = 0
    else:
        dmg = damage[i]-dist
    q.append((hp-max(0,dmg//2),i+1,dist,ult))
    q.append((hp-max(0,(dmg-k)),i+1,dist+k,ult))
    if ult == 1:
        q.append((hp-max(0,dmg),i+1,dist,2))

print(result)