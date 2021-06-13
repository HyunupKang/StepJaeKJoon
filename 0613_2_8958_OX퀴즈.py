T = int(input())
for i in range(T):
  a = input()
  Score = 0
  Score_sum = 0
  for j in a:
    if j == 'O':
      Score += 1
    else:
      Score = 0
    Score_sum += Score
  print(Score_sum)

#  for문에서 range 대신 a로 했음. 그러면 j는 차례대로 a의 문자열 인텍스에 대한 값  