# 프로그래머스
'''
1. 1->2,0
2. 2->3,1 / 0->1,-1
3. 3->4,2 / 1->2,0 / 1 -> 2,0 / -1 -> 0, -2
4  ....

'''


# bfs 풀이
from collections import deque

def solution(numbers, target):
    q = deque()
    q.append([numbers[0],0])
    q.append([numbers[0]*-1,0])
    answer = 0
    n = len(numbers)
    
    while q:
        print(q)
        tem, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([tem + numbers[idx],idx])
            q.append([tem - numbers[idx],idx])
        
        else:
            if tem == target:
                answer += 1
            
    
    return answer

# dfs 풀이
answer = 0
def dfs(idx, numbers, target, value):
    global answer
    n = len(numbers)

    if idx == n:
        if value == target:
            answer += 1
            return
    else:
        dfs(idx+1,numbers,target,value+numbers[idx])
        dfs(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
        
    dfs(0,numbers, target,0)
    
    return answer