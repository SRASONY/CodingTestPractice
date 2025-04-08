from collections import deque

N,K = map(int,input().split())
time = [0]*100001

def bfs(n,k):
    if n == k:
        return 0
    queue = deque([n])
    while queue:
        X = queue.popleft()
        for nx in [X-1,X+1,2*X]:
            if 0 <= nx <= 100000 and time[nx]==0:
                time[nx] = time[X]+1
                if nx == k:
                    return time[nx]
                queue.append(nx)

print(bfs(N,K))


