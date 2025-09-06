import math
H,W,M,N = map(int,input().split())

x,y = 0,0

x = math.ceil(H/(M+1))
y = math.ceil(W/(N+1))

print(x*y)