# 약수 게임
# Gold 3, math, game_theory

n,c = int(input()),0

for i in range(2,int(n**0.5)+1):
    while n%i == 0:
        n //= i
        c += 1
    if c > 2: break
if n > 1: c += 1

print('cubelover' if c == 2 else 'koosaga')