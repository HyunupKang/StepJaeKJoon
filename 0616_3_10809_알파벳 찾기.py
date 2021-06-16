word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 

# 아스키 코드에서 a=97이고 z=122이다. 
# find 함수는 어떤 찾는 문자가 문자열안에서 첫 번째 위치한 순서를 숫자로 출력
# 만약 없으면 -1 출력함.
# find함수는 문자열에서만 사용 가능

# 먼저 word가 asdf로 입력하고,
# alphabet 범위가 97~100이라면
# alphabet = [97, 98, 99]

# 4번째 반복문에서 첫번째 루틴이라면 x는 97
# 5번째줄에서 97을 아스키 코드로 변환하고, 이 아스키 코드를 word에 있는지 find
# 있으면 가장 첫번째 인덱스를 출력하고(여기선 첫번째에 있으니 0)
# 없으면 -1