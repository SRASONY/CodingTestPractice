import sys
input = sys.stdin.readline

# 입력 받기
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 가장 왼쪽과 오른쪽 벽 찾기
left, right = blocks[0], blocks[-1]

# 가장 높은 블록(nw)과 그 위치(nw_idx) 찾기
nw_idx = 0
nw = 0
for i in range(W):
    if blocks[i] > nw:
        nw = blocks[i]
        nw_idx = i

water = 0  # 누적 빗물

# 1. 왼쪽 -> 가장 높은 벽(nw_idx) 사이의 빗물 계산
left_max = blocks[0]
for i in range(1, nw_idx):
    if blocks[i] > left_max:
        left_max = blocks[i]
    else:
        water += left_max - blocks[i]

# 2. 오른쪽 -> 가장 높은 벽(nw_idx) 사이의 빗물 계산 (거꾸로)
right_max = blocks[-1]
for i in range(W - 2, nw_idx, -1):
    if blocks[i] > right_max:
        right_max = blocks[i]
    else:
        water += right_max - blocks[i]

print(water)
