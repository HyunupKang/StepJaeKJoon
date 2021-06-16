num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)

# 범위 선택 연산자를 [::01]로 지정해서 문자 배열을 뒤집어서 반환(int 타입은 불가능)
# 숫자 타입은 문자열처럼 분리해서 사용할 수 없어서 먼저 변환하고서 숫자로 변환