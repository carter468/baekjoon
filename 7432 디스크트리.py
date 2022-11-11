# 디스크 트리

import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self,path):
        curr_node = self.root
        for x in path:
            if x not in curr_node:
                curr_node[x] = {}
            curr_node = curr_node[x]
        curr_node['end'] = {}

    def answer(self,floor,curr_node=None):
        if floor == 0:
            curr_node = self.root
        for x in sorted(curr_node.keys()):
            if x != 'end':
                print(' '*floor,x,sep='')
            self.answer(floor+1,curr_node[x])

trie = Trie()
n = int(input())
for _ in range(n):
    a = list(map(str,input().strip().split('\\')))
    trie.insert(a)
trie.answer(0)