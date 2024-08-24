N= int(input()) # 사람의 수
P = list(map(int,input().split())) # 인츨하는데 걸리는 시간

P.sort()

answer =0 
C = 0 
for i in range(N):
    C += P[i]
    answer +=C

print(answer)