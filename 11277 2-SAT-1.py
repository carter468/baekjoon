# 2-SAT - 1

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
clause = []
for _ in range(m):
    i,j = map(int,input().split())
    clause.append([i,j])

def make(case):
    if len(case) == n+1:
        check(case)
        return
    for i in range(2):
        make(case+[i])

def check(case):
    for i,j in clause:
        if i>0:
            a = case[i]
        else:
            a = not case[-i]
        if j>0:
            b = case[j]
        else:
            b = not case[-j]
        if (a or b) == 0:
            return
    print(1)
    exit()

make([0])
print(0)