n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0  # 그룹 단어가 아닌 경우를 찾는데 사용
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)

# 예시로 ccazzzzbb
# 0번 인덱스와 1번 인덱스는 c로 같음 => error=0이므로 group_word + 1
# 1번 인덱스와 2번 인덱스는 c와 a로 다름 => new_word에 c이후 문자열 대입(따라서 new_word는 azzzzbb)
# 남은 문자열에서 현재 글자가 있는지 체크, 있다면 error+1. 
# error가 0이 아니면 grout_word 카운트 안함