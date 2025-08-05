from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
answer = []

heights = set()
heights.add(0)
for i in range(N):
    for j in range(N):
        heights.add(graph[i][j])

def bfs(x,y,a):
    queue = deque([(x,y)])
    visited[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and graph[nx][ny]>a:
                visited[nx][ny] = 1
                queue.append((nx,ny))

for h in heights:
    cnt =0
    visited = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0 and graph[i][j]>h:
                bfs(i,j,h)
                cnt +=1
    answer.append(cnt)

print(max(answer))