# 민식어
# Gold 5, 정렬

import sys
input = sys.stdin.readline
alphabet = ('a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y')

result = []
word = []
for t in range(int(input())):
    s = input().strip()
    word.append(s)
    for i in range(20):
        s = s.replace(alphabet[-1-i],chr(84-i))
    result.append((s,t))

for r in sorted(result):
    print(word[r[1]])