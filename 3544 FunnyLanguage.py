# Funny Language
# Gold 1, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

def letters_count(word):
    count = [0]*26
    for ch in word:
        count[ord(ch)-ord('A')] += 1
    return count

def check(a,b):
    for i in range(26):
        if a[i] > b[i]:
            return False
    return True

def count(word,indices,letters):
    cur = letters_count(word)
    res = []
    for idx in indices:
        if check(cur,letters[idx]):
            res.append(idx)
    return res

def push(word,indices):
    if word in visited:
        return
    visited.add(word)

    new_indices = count(word,indices,letters)
    if new_indices:
        heapq.heappush(pq,(-len(new_indices),word,new_indices))

n,m = map(int, input().split())
words = [input().strip() for _ in range(m)]

letters = [letters_count(w) for w in words]
pq = []
visited = set()
result = set()
push('',list(range(m)))

while pq and len(result) < n:
    _,word,indices = heapq.heappop(pq)

    if word and word not in words:
        result.add(word)

    for i in range(26):
        push(word+chr(ord('A')+i),indices)

s = ''
while len(result) < n:
    s += 'A'
    result.add(s)

print(*result,sep='\n')