#0818_1_카펫
'''
1. 브라운은 테두리 색 => 브라운 갯수 = 2*가로 + (세로-2)*2
2. 옐로우는 가로*세로 - 브라운
3. 카펫의 가로 길이는 세로보다 크거나 같으니, 가로부터 for문으로 브라운 수 체크
4. 브라운수 구하고 옐로우 갯수가 같으면 정답
'''
def solution(brown, yellow):
    answer = []
    for i in range(1, 5001):
        for j in range(1, i+1):
            if 2*(i+j-2) == brown:
                if i*j - brown == yellow:
                    answer.append(i)
                    answer.append(j)
            
    return answer