# 유기농 배추
from collections import deque

def bfs(x,y,graph):
    queue = deque([(x,y)]) # 초기위치 큐 삽입
    graph[x][y] = 0 # 초기위치 방문처리
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<M and 0<=ny<N and graph[nx][ny]==1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

T = int(input()) # 테스트케이스 개수
for i in range(T):
    M,N,K = map(int,input().split()) # 가로,세로,배추개수
    graph = [[0]* N for _ in range(M)]
    for j in range (K):
        X,Y = list(map(int,input().split())) # 배추 위치
        graph[X][Y]=1

    cnt = 0 # 배추흰지렁이 마리 수
    for i in range(M):
        for j in range(N):
            if graph[i][j]==1:
                cnt +=1 
                bfs(i,j,graph)  
    print(cnt)