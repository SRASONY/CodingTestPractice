def solution(friends, gifts):
    answer = 0
    l = len(friends)
    table = [[0]*l for _ in range(l)]
    count = [0] * l
    result = [0] * l

    for gift in gifts:
        give,take = gift.split()

        give_idx = friends.index(give)
        take_idx = friends.index(take)

        table[give_idx][take_idx] +=1

        count[give_idx]+=1
        count[take_idx]-=1
    print(table)
    print(count)


    for i in range(l):
        for j in range(i,l):
            if table[i][j] < table[j][i]:
                result[j] +=1
            elif table[i][j] > table[j][i]:
                result[i] +=1
            elif (table[i][j] ==0 and table[j][i] == 0) or (table[i][j] == table[j][i]):
                if count[i]>count[j]:
                    result[i]+=1
                elif count[i]<count[j]:
                    result[j]+=1
    print(result)
    answer = max(result)
    return answer