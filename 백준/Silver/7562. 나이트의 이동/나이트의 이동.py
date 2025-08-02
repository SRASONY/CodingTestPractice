from collections import deque

def bfs():
    queue = deque([(cx,cy)])
    chess[cx][cy] = 1

    dx = [-2,-2,2,2,1,-1,1,-1]
    dy = [1,-1,1,-1,2,2,-2,-2] 

    while queue:
        x,y = queue.popleft()
        if x == ax and y == ay:
            return chess[x][y] -1
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<I and 0<=ny<I and chess[nx][ny] == 0:
                queue.append((nx,ny))
                chess[nx][ny] = chess[x][y]+1


T = int(input())
for _ in range(T):
    I = int(input())
    cx,cy = map(int,input().split())
    ax,ay = map(int,input().split())
    chess = [[0]*I for _ in range(I)]
    print(bfs())