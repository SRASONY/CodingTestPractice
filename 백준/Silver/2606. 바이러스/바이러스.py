computers = int(input())
n = int(input())
network = [[] for _ in range(computers+1)] 
visited = [0]*(computers+1)
cnt = 0

for _ in range(n):
    a,b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)

def dfs (graph,v):
    global cnt
    visited[v] =1
    cnt +=1
    for i in graph[v]:
        if visited[i] ==0:
            dfs(graph,i)
    return cnt -1

print(dfs(network,1))