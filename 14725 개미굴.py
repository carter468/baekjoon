# 개미굴

import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self,feed):
        curr_node = self.root
        for x in feed:
            if x not in curr_node:
                curr_node[x] = {}
            curr_node = curr_node[x]
        curr_node['end'] = {}

    def ans(self,floor,curr_node=None):
        if floor == 0:
            curr_node = self.root
        for x in sorted(curr_node.keys()):
            if x != 'end':
                print('--'*floor,x,sep='')
            self.ans(floor+1,curr_node[x])

trie = Trie()
N = int(input())
for _ in range(N):
    a = list(map(str,input().split()))
    trie.insert(a[1:])
trie.ans(0)
