# Mix and Build
# Gold 2, DP, hash set

from collections import defaultdict
import sys
input = sys.stdin.readline

origin = defaultdict(str)
arr = []
while True:
    try: 
        s = input().strip()
        if not s: break
    except: break
    ss = ''.join(sorted(s))
    arr.append(ss)
    origin[ss] = s
perm = set(arr)

arr.sort(key=lambda x:len(x))
dp = defaultdict(int)
parent = defaultdict(str)
result = [0,arr[0]]
for s in arr:
    for i in range(26):
        ns = ''.join(sorted(s+chr(i+97)))
        if ns in perm and dp[ns] < dp[s]+1:
            dp[ns] = dp[s]+1
            parent[ns] = s
            if dp[ns] > result[0]: result = [dp[ns],ns]

s = result[1]
answer = [origin[s]]
while parent[s]:
    s = parent[s]
    answer.append(origin[s])
print(*answer[::-1],sep='\n')