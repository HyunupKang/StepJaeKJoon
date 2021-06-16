croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수가 있으면 *출력
print(len(word))

# replace()는 함수를 사용한 문자열 원형을 변형시키지 않는 비파괴 함수임
# 예를들어
#>>> for i in croatia :
#>>>     word2 = word.replace(i, '*')  # input 변수와 다른 이름의 변수
#>>>     print(word2)
#>>> print(len(word2))
# 와 같이 입력변수와 다른 변수이름에 저장하면

#ljes=njak
#ljes=njak
#ljes=njak
#ljes=njak  <---
#*es=njak    <---
#ljes=*ak  <-----
#lje*njak
#ljes=njak
#9
#처럼 원형이 계속 남아있음
# 그래서 word = word.replace(i, '*') 처럼 동일 변수에 선언해야 함