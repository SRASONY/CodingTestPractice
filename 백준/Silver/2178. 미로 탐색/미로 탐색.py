from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])  # 시작점을 큐에 추가

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0] # 상하좌우
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
    return graph[N-1][M-1]
            
    
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(0, 0))
