from collections import deque

F,S,G,U,D = map(int,input().split())
buttons = [0]*(F+1)
def bfs(s,g,u,d):
    if s == g:
        return 0
    queue = deque([s])
    buttons[s] =1
    while queue:
        S = queue.popleft()
        for ns in [S+u,S-d]:
            if 1<=ns<=F and buttons[ns]==0:
                buttons[ns] = buttons[S]+1
                if ns == g:
                    return buttons[ns]-1
                queue.append(ns)
    return "use the stairs"
print(bfs(S,G,U,D))