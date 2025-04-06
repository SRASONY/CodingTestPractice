from collections import deque

def bfs(tomatoes):
    days =0
    queue = deque()

    # 처음부터 익은 토마토 전부 큐에 넣기 --> 동시에 하기 위해
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if tomatoes[z][x][y] == 1:
                    queue.append((z, x, y))

    dx = [-1,1,0,0,0,0] # 상하
    dy = [0,0,-1,1,0,0] # 좌우
    dz = [0,0,0,0,1,-1] # 위아래

    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nz = z+dz[i]
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nz<H and 0<=nx<N and 0<=ny<M and tomatoes[nz][nx][ny] == 0:
                queue.append((nz,nx,ny))
                tomatoes[nz][nx][ny]=tomatoes[z][x][y]+1

        # 결과 출력 (안 익은 토마토 확인)
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if tomatoes[z][x][y] == 0:
                    return -1
                days = max(tomatoes[z][x][y],days)
    return days-1

M,N,H = map(int,input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs(tomatoes))

