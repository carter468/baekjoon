# XOR 수열
# Platinum 3, trie, greedy

N = int(input()).bit_length()
input()
A = tuple(map(int,input().split()))

count = [[0]*2 for _ in range(N)]
trie = [[-1,-1,0]]
for a in A:
    cur = 0
    for i in range(N-1,-1,-1):
        trie[cur][2] += 1
        l,r = trie[cur][:2]

        if a>>i&1 == 0:
            if r != -1:
                count[i][1] += trie[r][2]
            if trie[cur][0] == -1:
                trie[cur][0] = len(trie)
                trie.append([-1,-1,0])
            cur = trie[cur][0]
        else:
            if l != -1:
                count[i][0] += trie[l][2]
            if trie[cur][1] == -1:
                trie[cur][1] = len(trie)
                trie.append([-1,-1,0])
            cur = trie[cur][1]
    trie[cur][2] += 1

print(sum(max(c) for c in count))