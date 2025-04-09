from collections import deque

N = int(input())
location = [list(map(int,input().split())) for _ in range(N)]
height = max(map(max,location))
cnt_list = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,visited,h):
    queue = deque([(i,j)])
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and location[nx][ny] > h:
                    visited[nx][ny] =1
                    queue.append((nx,ny))

for h in range(0,height+1):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 아직 방문 안했고 잠기지 않았다면 새 영역의 시작점
            if not visited[i][j] and location[i][j] > h:
                bfs(i,j,visited,h)
                cnt +=1
    cnt_list.append(cnt)

print(max(cnt_list))