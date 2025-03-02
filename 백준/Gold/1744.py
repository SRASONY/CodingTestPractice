# 1. 1보다 큰 수의 경우 큰 수부터 정렬한 후 2개씩 곱해서 답에 더한다.
# 2. 1인 경우는 무조건 곱보다 합이 이득이기 때문에 바로 답에 더한다.
# 3. 0보다 작거나 같은 경우 더 작은 수 부터 2개씩 곱해서 답에 더한다.

import sys
input = sys.stdin.readline
N = int(input())

numbers = list(int(input()) for _ in range(N))
plus = []
minus = []
result = 0

for num in numbers :
    if num > 1:
        plus.append(num)
    elif num ==1:
        result +=num
    else :
        minus.append(num)
plus.sort(reverse=True)
minus.sort()

for i in range (0,len(plus),2):
    if i+1<len(plus):
        result+=plus[i]*plus[i+1]
    else:
        result+=plus[i]

for i in range(0,len(minus),2):
    if i+1<len(minus):
        result+=minus[i]*minus[i+1]
    else:
        result+=minus[i]
print(result)