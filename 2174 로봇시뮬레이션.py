# 로봇 시뮬레이션
# Gold 5, implementation, simulation

c,r = map(int,input().split())
n,m = map(int,input().split())

robot = [['0']]
grid = [[0]*c for _ in range(r)]
for i in range(n):
    y,x,d = input().split()
    y,x = int(y)-1,int(x)-1
    robot.append([x,y,{'E':0,'S':1,'W':2,'N':3}[d]])
    grid[x][y] = i+1

def move():
    for i,cmd,t in [input().split() for _ in range(m)]:
        i,t = int(i),int(t)
        if cmd == 'L':
            robot[i][2] = (robot[i][2]-t)%4
        elif cmd == 'R':
            robot[i][2] = (robot[i][2]+t)%4
        else:
            x,y = robot[i][:2]
            grid[x][y] = 0
            dx,dy = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}[robot[i][2]]
            for _ in range(t):
                x += dx
                y += dy
                if x < 0 or x == r or y < 0 or y == c:
                    return f'Robot {i} crashes into the wall'
                if grid[x][y] != 0:
                    return f'Robot {i} crashes into robot {grid[x][y]}'
            grid[x][y] = i
            robot[i][0],robot[i][1] = x,y
    return 'OK'

print(move())