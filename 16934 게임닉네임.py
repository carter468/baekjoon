# 게임 닉네임
# Gold 3, trie

import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.children = {}

    def add(self,name):
        idx,flag = len(name),False
        curr_node = self.children
        for i,x in enumerate(name):
            if x not in curr_node:
                curr_node[x] = {}
                if flag == False:
                    idx = i+1
                    flag = True
            curr_node = curr_node[x]
        print(name[:idx])

dic = {}
trie = Trie()
for _ in range(int(input())):
    s = input().strip()
    if s in dic:
        dic[s] += 1
        print(s+str(dic[s]))
    else:
        dic[s] = 1
        trie.add(s)