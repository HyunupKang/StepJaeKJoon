#0818_2_모의고사
'''
'''
def solution(answers):
    answer = []
    score1, score2, score3 = 0, 0, 0

    Num1 = [1, 2, 3, 4, 5] # 5
    Num2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    Num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    idx = 0
    for i in answers:
        if Num1[idx%5] == i: 
            score1 += 1
        if Num2[idx%8] == i: 
            score2 += 1
        if Num3[idx%10] == i: 
            score3 += 1
        idx += 1
        
    an = []
    an.append(score1)
    an.append(score2)
    an.append(score3)    
    
    for i in range(3):
        if max(an) == an[i]:
            answer.append(i+1)

    answer.sort()
    return answer