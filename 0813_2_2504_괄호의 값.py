#0813_2_2504_괄호의 값
'''
1. 괄호열이 아니라면 0출력
2. 괄호열이 맞다면 괄호가 닫힐때 점수 부여
3. 닫힐 때 바로 닫히면 점수 +
4. stack에 점수가 있을 시, 닫힐때 점수 *
'''
import sys

str_input = list(map(str, sys.stdin.readline()))
stack = []
score = 0


for i in str_input:
    if i == '(' or i == '[':
        stack.append(i)
    elif (i == ')' or i == ']') and stack:            
        if stack[-1] == '(' and i == ')':
            del stack[-1]
        elif stack[-1] == '[' and i == ']':
            del stack[-1]
    elif not stack and (i == ']' or i == ')'):
        stack.append(i)
        break
if stack:
    print(0) 
else:
    stack=[]
    for i in str_input:
        if i == '(' or i == '[':
            stack.append(i)
        else:# 올바른 괄호열이기 때문에 숫자만 있듬
            if i == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:       
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1): # 괄호 만날때 까지 계속 더하기, (index 마지막부터, 0까지, -1씩)
                        if stack[idx] == '(':
                            stack[-1] = temp*2
                            break
                        else:
                            
                            temp += stack[-1] # 임시 변수에 stack의 마지막 숫자를 더함
                            stack.pop()         # 더한 숫자 빼기

            elif i == ']':
                if stack[-1] == '[':
                    stack[-1] = 3
                else:       # 올바른 괄호열이기 때문에 숫자만 있듬
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1): # 괄호 만날때 까지 계속 더하기, (index 마지막부터, 0까지, -1씩)
                        if stack[idx] == '[':
                            stack[-1] = temp*3
                            break
                        else:
                            temp += stack[-1] # 임시 변수에 stack의 마지막 숫자를 더함
                            stack.pop()         # 더한 숫자 빼기
    print(sum(stack))