'''
1. 문자열을 리스트로 변환
2. 문자열 리스트에서 1~len(문자열)까지 순열
3. 중복 제거 후, 다시 리스트로.
4. 순열 리스트에서 하나씩 소수인지 검사.
5. 소수 검사에서는 제곱수까지 범위를 하면 됨
'''

from itertools import permutations
import math

def check(num):
    k=math.sqrt(num)   # <<<<<---- 소수 찾을 땐, 제곱수까지!!
    
    if num < 2:
        return False
    
    for i in range(2, int(k)+1):
        if num % i == 0:
            return False
    return True

        
def solution(numbers):
    answer = [] # 중복 제거하기 위해
    
    for k in range(1, len(numbers)+1):
        num_list = list(map(''.join, permutations(list(numbers), k)))  # <<<-- 순열을 리스트로 만드는 기법!!!
        for num in list(set(num_list)):  # <<<<---- 중복 제거를 놓쳤다.
            if check(int(num)):
                answer.append(int(num))
                
    answer = len(set(answer))
    return answer