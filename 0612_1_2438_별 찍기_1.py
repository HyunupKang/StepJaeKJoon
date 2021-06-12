inp = int(input())
for i in range(1,(inp+1)):
    print("*" * i)


T = int(input())

for i in range(1, T+1):
  for j in range(1, i+1):  
    print("*",end="")
  print()

  #아래는 c처럼 코드를 짠 것,
  #위는 3라인이 파이썬의 장점을 활용한 것