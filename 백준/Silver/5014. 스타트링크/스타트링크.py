from collections import deque
F,S,G,U,D = map(int,input().split())
elevator = [0]*(F+1)

def bfs(f,s,g,u,d):
    if s == g:
        return 0
    queue = deque([s])
    elevator[s] =1
    while queue:
        s = queue.popleft()
        for i in [s+u,s-d]:
            ns = i   
            if 0<ns<=f and elevator[ns]==0:
                elevator[ns]=elevator[s]+1
                if ns == g:
                    return elevator[ns]-1
                queue.append(ns)
    else:
        return("use the stairs")
print(bfs(F,S,G,U,D))

