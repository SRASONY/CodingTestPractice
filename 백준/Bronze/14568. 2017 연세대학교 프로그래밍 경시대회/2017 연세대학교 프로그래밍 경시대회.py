candy = int(input())
cnt = 0

for i in range(2,candy+1,2): # 택희
    for j in range(1,candy-i): # 영훈
        k = candy-i-j # 남규
        if k >=j+2:
            cnt+=1
print(cnt)

