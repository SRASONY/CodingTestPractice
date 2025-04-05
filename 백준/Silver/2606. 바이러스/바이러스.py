from collections import deque

N = int(input()) # 컴퓨터 수
M = int(input()) # 연결 수
graph = [[] for _ in range(N+1)] # 인덱스 0 안씀(인덱스 = 컴퓨터 번호)
visited = [0]*(N+1)

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x) # 양방향 연결

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    cnt = 0
    while queue:
        cur = queue.popleft()
        for a in graph[cur]:
            if not visited[a]:
                queue.append(a)
                visited[a] = 1
                cnt +=1
    return cnt

print(bfs(1))
