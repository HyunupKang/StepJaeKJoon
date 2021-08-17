'''
1. 스택 선언
2. 스택에 값이 있고, 스택 끝 값이 새로 들어올 수보다 작고, 빼는 횟수가 존재한다면
3. 스택 끝 값을 뺀다.
4. 2번 반복.
5. 새로 들어올 수가 스택 끝 값보다 작을 경우, 새로 들어올 수를 append
6. 빼는 횟수가 여유일 경우
7. 뒷 부분부터 삭제
'''

def solution(number, k):
    answer = ''
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0: # <<<<<< int형으로 변환 안해줘도 비교 가능!!!!!!!!!
            stack.pop()
            k -= 1
        
        stack.append(num)
    if k > 0:   # <<< ---- "999", k=2 일때 상황
        for _ in range(k):
            stack.pop()
    answer = ''.join(stack)
    return answer    