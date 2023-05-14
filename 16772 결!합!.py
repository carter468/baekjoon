# 결! 합!
# Gold 4, 브루트포스

import sys
input = sys.stdin.readline

def check():
    for l in range(3):
        if card[i][l]==card[j][l]==card[k][l] or (card[i][l]!=card[j][l] and card[j][l]!=card[k][l] and card[k][l]!=card[i][l]): continue
        return False
    return True

card = [input().split() for _ in range(9)]
hap = set()

for i in range(9):
    for j in range(i+1,9):
        for k in range(j+1,9):
            if check():
                hap.add((i+1,j+1,k+1))

score = 0
gyeol = False
for _ in range(int(input())):
    a = input().split()
    if a[0] == 'G':
        if not hap and not gyeol:
            score += 3
            gyeol = True
        else:
            score -= 1
    else:
        b = tuple(sorted(map(int,a[1:])))
        if b in hap:
            score += 1
            hap.remove(b)
        else:
            score -= 1
        
print(score)