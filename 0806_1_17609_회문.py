#0806_1_17609_회문
'''
1. 문자열의 가장 왼쪽과 오른쪽을 비교.
2. 두번째의 왼쪽과 오른쪽을 비교.
3. 계속해서 비교하다가 왼쪽 숫자와 오른쪽 숫자가 교차되면 회문
4. 왼쪽/오른쪽이 다르면 왼쪽 +1과 오른쪽을 비교해보고 or 왼쪽과 오른쪽-1을 비교
5. 교차되면 유사회문, 아니면 단순 문자열

'''

def check(left, right):
    while left < right:
        if s[left] == s[right]:
            left +=1
            right -=1
        else:
            return False
    return True

def TwoPointer(left, right):
    while left < right:
        if s[left] == s[right]:
            left +=1
            right -=1
        else:
            if check(left+1, right) or check(left, right-1):
                return 1
            return 2
    return 0

T = int(input())

for _ in range(T):
    s = input()
    print(TwoPointer(0, len(s)-1))




# import copy
# T = int(input())

# def Similar(s):
    
#     for i in range(len(s)):
#         temp  = copy.deepcopy(s)
#         s.pop(i)
#         strin2 = ''.join(reversed(s))    
#         s = temp
#         strin_re = ''.join(reversed(strin2))

#         if strin2 == strin_re:
#             return 1
        
#     return 0




# for _ in range(T):
#     strin = list(input())
#     strin2 = ''.join(reversed(strin))    
#     strin_re = ''.join(reversed(strin2))

#     if strin2 == strin_re:
#         print(0)
#     elif Similar(strin):
#         print(1)
#     else:
#         print(2)