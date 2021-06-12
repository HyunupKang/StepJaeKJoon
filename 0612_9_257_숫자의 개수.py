A = int(input())
B = int(input())
C = int(input())

ABC = list(str(A*B*C))

for i in range(10):
  print(ABC.count(str(i)))

  # a,b,c 곱을 문자열로 변환후 리스트로 묶는다.
  # ex) ABC = list("170373300")
  #     ABC = [1,7,0,3,7,3,3,0,0]

  # 정수를 문자열로, 문자열을 리스트로, 리스트의 i번쨰 요소를 문자열로,
  # 문자열 함수인 count를 이용