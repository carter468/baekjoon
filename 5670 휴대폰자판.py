# 휴대폰자판

import sys
input = sys.stdin.readline

class Node:
    def __init__(self,data):
        self.data = data
        self.child = {}
        self.flag = False

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self,word):
        curr = self.head
        for x in word:
            if x not in curr.child:
                curr.child[x] = Node(x)
            curr = curr.child[x]
        curr.flag = True
    
    def counting(self,word):
        curr = self.head
        cnt = 0
        for x in word:
            if curr == self.head:
                cnt += 1
            elif len(curr.child) > 1 or curr.flag == True:
                cnt += 1
            curr = curr.child[x]
        return cnt

while True:
    trie = Trie()
    words = []
    try:
        N = int(input())
    except:
        break
    for _ in range(N):
        s = input().rstrip()
        trie.insert(s)
        words.append(s)
    ans = 0
    for x in words:
        ans += trie.counting(x)

    print('{:.2f}'.format(ans/N))