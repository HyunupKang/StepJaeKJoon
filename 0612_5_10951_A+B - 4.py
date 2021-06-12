while True:
  try:
    A, B = map(int, input().split())
    print(A+B)
  except:
    break

#예외 상항 처리,
#숫자가 입력되지 않으면 except 구문으로 빠져서 반복문 탈출    