'''
1. 위치와 값 리스트에 저장
2. 가장 앞 리스트가 최대값인지 확인
3. 최대값이라면 인쇄와 answer + 1, 아니라면 맨 뒤에 append
'''
def solution(priorities, location):  # 중요도, 요청 대기 번호
    answer = 0
    q = []
    for i in range(len(priorities)):
        q.append([priorities[i], i])
        
    while q:
        dacu, idx = q.pop(0)
        temp = priorities.pop(0)
        
        if q and max(priorities) > dacu:
            q.append([dacu, idx])
            priorities.append(temp)                
        else:  # 인쇄할때 answer + 1
            answer += 1
            if location == idx:
                break
                
    return answer