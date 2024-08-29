# 그림
from collections import deque
    
def bfs (x,y):
    queue = deque([(x,y)]) # 시작점을 큐에 추가 - 튜플형태
    graph[x][y] = 0 # 시작점 방문 처리 (1을 0으로 바꾸어 방문 표시)
    size = 1 # 그림의 초기 크기 (현재 점 포함)

    dx = [0,0,-1,1] # 좌우 이동
    dy = [-1,1,0,0] # 상하 이동

    while queue:
        x,y = queue.popleft() # 큐에서 좌표 꺼냄
        for i in range(4): # 상하좌우 네방향 탐색
            nx = dx[i]+x # 새로운 x좌표
            ny = dy[i]+y # 새로운 y좌표

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 :
                # 배열 범위 내에 있고, 방문하지 않은 1인 경우
                queue.append((nx,ny)) # 큐에 새 좌표 추가
                graph[nx][ny] = 0 # 방문 처리
                size +=1 #그림 크기 증가
    return size


n,m = map(int,input().split()) # 세로,가로 길이
graph = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1 # 그림의 개수
            max_size = max(bfs(i,j),max_size) #그림의 최대 크기

print (cnt)
print (max_size)