N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

for i in range(N):
    # 상담을 안 했을 경우, 다음 날까지 수익 유지
    dp[i + 1] = max(dp[i + 1], dp[i])
    
    # 상담을 했을 경우, 끝나는 날의 수익 업데이트
    end_day = i + T[i]
    if end_day <= N:
        dp[end_day] = max(dp[end_day], dp[i] + P[i])

print(dp[N])
