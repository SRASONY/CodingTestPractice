# 토마토
from collections import deque

def bfs():
    queue = deque([]) # 시작점을 큐에 추가

    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                queue.append((i,j))

    dx =[0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            if 0<=nx<N and 0<=ny<M and graph[nx][ny] ==0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return max(max(row) for row in graph)

M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

answer = bfs()


for boxes in graph:
    for tomato in boxes:
        if tomato == 0:
            print(-1)
            exit(0)

print(answer-1)


