num = list(map(int,input()))
zero = 0
one = 0

if num[0] == 0:
    zero +=1
else: one +=1

for i in range(len(num)-1):
    if num[i]!=num[i+1]:
        if num[i+1] == 0:
            zero+=1
        else:
            one+=1

print(min(zero,one))