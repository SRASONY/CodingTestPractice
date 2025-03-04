import sys
input= sys.stdin.readline

dp =[0]*1001
dp[1],dp[2],dp[3] = 1,2,4
for i in range(4,1001):
    dp[i]= dp[i-3]+dp[i-2]+dp[i-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
