import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))  # 정렬된 리스트
good = 0

for i in range(N):
    seen = set()  # 이전에 나온 A[j] 값을 저장
    for j in range(N):
        if i == j:
            continue  # 자기 자신을 포함하면 안 됨

        if A[i] - A[j] in seen:  # A[j]와 다른 이전 수들의 합이 A[i]가 되는지 체크
            good += 1
            break  # 중복 카운트 방지

        seen.add(A[j])  # 현재 A[j]를 저장

print(good)
