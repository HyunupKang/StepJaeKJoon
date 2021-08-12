#0813_1_1138_한 줄로 서기
'''
키에 따른(people의 index) 값은 곧 줄의 앞에서부터 카운트 될 0의 갯수.
'''
n = int(input()) # 사람의 수
people = list(map(int, input().split())) # 크기 순으로 왼쪽에 자기보다 큰 사람이 몇명인지.
jul = [0]*n

for i in range(n):
    step = people[i]
    cnt = 0
    for j in range(n):
        if jul[j]==0 and cnt == step:
            jul[j] = i+1
            break
        elif jul[j] == 0:
            cnt += 1    

print(' '.join(map(str, jul)))