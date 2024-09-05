# 단지 내 번호 붙이기
from collections import deque

N = int(input()) # 지도의 크기 : N * N
graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(x,y):
    queue = deque([(x,y)])
    graph[x][y] = 0 # 방문 처리
    house = 1 # 단지 내 집의 수
   
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                house +=1 
    return house

                
village = 0 # 단지 수
houses = []

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            houses.append(bfs(i,j))
            village +=1 
print(village)

houses.sort()
for house in houses:
    print(house)