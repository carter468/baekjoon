# 상범 빌딩
# Gold 5, BFS

from collections import deque

while True:
	l,r,c = map(int,input().split())
	if l == 0: break
	arr = []
	for _ in range(l):
		arr.append([input() for _ in range(r)])
		input()
	visited = [[[-1]*c for _ in range(r)] for _ in range(l)]
	for i in range(l):
		for j in range(r):
			for k in range(c):
				if arr[i][j][k] == 'S':
					q = deque([(i,j,k)])
					visited[i][j][k] = 0
	while q:
		x,y,z = q.popleft()
		if arr[x][y][z] == 'E':
			print(f'Escaped in {visited[x][y][z]} minute(s).')
			break
		for nx,ny,nz in (x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1):
			if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and visited[nx][ny][nz] == -1 and arr[nx][ny][nz] != '#':
				visited[nx][ny][nz] = visited[x][y][z]+1
				q.append((nx,ny,nz))
	else: print('Trapped!')