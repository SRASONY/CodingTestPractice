from collections import deque

def solution(numbers, target):
    answer = 0 
    n = len(numbers)
    queue = deque()
    queue.append((0,0))
    
    while queue:
        current_sum,idx = queue.popleft()
        
        if idx == n:
            if current_sum == target:
                answer+=1
        else:
            queue.append((current_sum+numbers[idx], idx+1))
            queue.append((current_sum-numbers[idx], idx+1))


    return answer
