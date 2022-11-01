# 숫자 할리갈리 게임

from collections import deque
import sys
input = sys.stdin.readline

# 덱 입력
number_card, number_game = map(int,input().split())
deck_do,deck_su = deque(),deque()
for _ in range(number_card):
    a,b = map(int,input().split())
    deck_do.append(a)
    deck_su.append(b)

# 게임 종료 판별
def checkEnd(n,m):
    if n==m:
        if len(deck_do) == len(deck_su):
            print('dosu')
        elif len(deck_do) > len(deck_su):
            print('do')
        else:
            print('su')
        quit()

# 게임 스타트
deck_ground_do,deck_ground_su = deque(),deque()
count_game = 0
while True:
    deck_ground_do.append(deck_do.pop())
    if not deck_do:
        print('su')
        break
    if deck_ground_do and deck_ground_su and deck_ground_do[-1]+deck_ground_su[-1] == 5:
        deck_su.extendleft(deck_ground_do)
        deck_su.extendleft(deck_ground_su)
        deck_ground_do.clear()
        deck_ground_su.clear()
    if (deck_ground_do and deck_ground_do[-1] == 5) or (deck_ground_su and deck_ground_su[-1] == 5):
        deck_do.extendleft(deck_ground_su)
        deck_do.extendleft(deck_ground_do)
        deck_ground_do.clear()
        deck_ground_su.clear()
    count_game += 1
    checkEnd(count_game,number_game)
    
    deck_ground_su.append(deck_su.pop())
    if not deck_su:
        print('do')
        break
    if deck_ground_do and deck_ground_su and deck_ground_do[-1]+deck_ground_su[-1] == 5:
        deck_su.extendleft(deck_ground_do)
        deck_su.extendleft(deck_ground_su)
        deck_ground_do.clear()
        deck_ground_su.clear()
    if (deck_ground_do and deck_ground_do[-1] == 5) or (deck_ground_su and deck_ground_su[-1] == 5):
        deck_do.extendleft(deck_ground_su)
        deck_do.extendleft(deck_ground_do)
        deck_ground_do.clear()
        deck_ground_su.clear()
    count_game += 1
    checkEnd(count_game,number_game)