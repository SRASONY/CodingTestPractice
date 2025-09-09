N = int(input())
channels = [input().strip() for _ in range(N)]
ans = []

# 1) KBS1을 맨 위(0)로
i1 = channels.index("KBS1")
ans.extend('1' * i1)   # 커서를 i1로
ans.extend('4' * i1)   # 위로 i1번 끌어올리기

# 2) KBS2의 현재 인덱스 계산(배열 변화 반영)
i2_orig = channels.index("KBS2")
if i2_orig > i1:
    i2 = i2_orig
else:
    i2 = i2_orig + 1   # KBS2가 위에 있었던 경우 한 칸 밀림

# KBS2를 두 번째(1)로
ans.extend('1' * i2)
ans.extend('4' * (i2 - 1))

print(''.join(ans))