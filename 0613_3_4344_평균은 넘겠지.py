T = int(input())
for i in range(T):
  score = list(map(int,input().split()))
  Midle_score = sum(score[1:])/score[0]
  cnt = 0
  for j in score[1:]:
    if j > Midle_score:
      cnt += 1
  rate = cnt/score[0]*100
  print(f'{rate:.3f}%')


# for문의 범위 조건 score[1:]에서 보듯, 시작 인덱스 설정 가능
# sum에서도 [1:]
# print문에서 소ㅜ점 자리 출력