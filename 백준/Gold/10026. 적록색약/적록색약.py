from collections import deque

N= int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]


non = 0
yes = 0


def bfs(x,y):

    queue = deque([(x,y)])
    visited[x][y] = 1

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[x][y]==graph[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                
    return

def bfs_yes(x,y):

    queue = deque([(x,y)])
    visited2[x][y] = 1

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[x][y]==graph[nx][ny] and visited2[nx][ny] == 0:
                visited2[nx][ny] = 1
                queue.append((nx,ny))
                
    return        

for i in range(N):
    for j in range(N):
        if (graph[i][j] in ['R', 'G', 'B']) and visited[i][j] == 0:
            non +=1
            bfs(i,j)

for i in range(N):
    for j in range(N):
        if graph[i][j] == "G":
            graph[i][j] = "R"

for i in range(N):
    for j in range(N):
        if (graph[i][j] in ['R','B']) and visited2[i][j] == 0:
            yes +=1
            bfs_yes(i,j)

print(non, yes)