alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
print(time)

# !!!다이얼 숫자에 해당하는 알파벳을 리스트에 저장!!
# 알파벳 리스트의 각 요소를 꺼내서 한글자씩 분리
# 입력받은 word 문자를 한글자씩 분리
# 꺼낸 문자를 비교