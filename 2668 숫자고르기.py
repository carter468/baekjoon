# 숫자고르기
# Gold 5, DFS

def dfs(x,start):
    if x == start:
        result.add(x)
        return True
    
    if not visited[x]:
        visited[x] = True
        if dfs(arr[x],start):
            result.add(x)
            return True

    return False

n = int(input())
arr = [0]*(n+1)
for i in range(n):
    arr[i+1] = int(input())

result = set()
for i in range(1,n+1):
    if i not in result:
        visited = [False]*(n+1)
        visited[i] = True
        dfs(arr[i],i)

print(len(result))
print('\n'.join(map(str,sorted(result))))