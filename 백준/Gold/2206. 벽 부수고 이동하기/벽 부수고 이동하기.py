from collections import deque
N,M = map(int,input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# visited[0][x][y] : 벽 안 부숨 (x=행, y=열)
# visited[1][x][y] : 벽 부숨
visited = [[[0]*M for _ in range(N)] for _ in range(2)] 

def bfs(a,b,used): # a=x(행), b=y(열)
    queue= deque([(a,b,used)])
    visited[used][a][b] = 1
    dx = [-1,1,0,0] 
    dy = [0,0,-1,1]
    while queue:
        x,y,z = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[z][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 0 and visited[z][nx][ny] == 0:
                    visited[z][nx][ny] = visited[z][x][y] + 1
                    queue.append((nx, ny, z))
                elif graph[nx][ny] == 1 and z == 0 and visited[1][nx][ny] == 0:
                    visited[1][nx][ny] = visited[z][x][y] + 1
                    queue.append((nx, ny, 1))
    return -1

print(bfs(0,0,0))