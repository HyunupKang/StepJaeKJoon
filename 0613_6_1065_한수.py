num = int(input())

hansu = 0

for i in range(1, num+1):
  num_list = list(map(int, str(i))) # 문자열로 변환시키고, 각 자리수를 분리해서 다시 int타입으로 변환. <--이게 좀 이해가 안되네, 어떻게 각 자리수가 분리된다는 거지
  if i < 100:
    hansu +=1  # 100보다 작으면 모두 한수
  elif num_list[0] - num_list[1] == num_list[1]-num_list[2]:
    hansu +=1  # x의 각 자리가 등차수열이면 한수
print(hansu)    