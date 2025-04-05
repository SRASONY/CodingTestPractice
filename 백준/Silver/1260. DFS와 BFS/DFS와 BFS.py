from collections import deque

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

visited1 = [0]*(N+1)
visited2 = [0]*(N+1)

def dfs(v):
    visited1[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if not visited1[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = 1

    while queue:
        cur = queue.popleft()
        print(cur, end = ' ')
        for i in graph[cur]:
            if not visited2[i]:
                visited2[i]=1
                queue.append(i)

dfs(V)
print()
bfs(V)