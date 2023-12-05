# 가희와 총선거 5
# Gold 3, implementation, parsing

from collections import defaultdict

def value(): return 99

def tier(x):
    if x < 17: return 1
    if x < 33: return 2
    if x < 49: return 3
    if x < 65: return 4
    if x < 81: return 5
    return 6

a = input().split()
arr1 = defaultdict(value)
i = 0
rank = 1
while len(arr1) != 80:
    name = []
    while i < len(a) and a[i] != 'Group':
        name.append(a[i])
        i += 1
    group = a[i+1]
    team = a[i+3]
    arr1[(group,team,' '.join(name))] = rank
    rank += 1
    i += 4

a = input().split()
arr2 = defaultdict(value)
i = 0
rank = 1
while len(arr2) != 80:
    name = []
    while i < len(a) and a[i] != 'Group':
        name.append(a[i])
        i += 1
    group = a[i+1]
    team = a[i+3]
    arr2[(group,team,' '.join(name))] = rank
    rank += 1
    i += 4

p = 0
for player in arr1:
    if arr1[player] < 17 and arr2[player] > 16:
        p += 1

result = [0]
for player in arr2:
    score = 0

    x = tier(arr1[player])
    y = tier(arr2[player])
    if x > y: score += 10000*(x-y)

    if arr2[player] in (1,17,33,49,65):
        if score: score += 20000
        else: score += 10000

    if x != 1 and y == 1:
        score += 30000*p
        
    if score > result[0]:
        result = [score,arr2[player],player]
    elif score == result[0] and arr2[player] < result[1]:
        result = [score,arr2[player],player]

print('\n'.join(result[2]))