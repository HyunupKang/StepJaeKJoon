numbers = list(range(1,10001))
remove_list = []

for num in numbers:         #만약 현재 numbers가 10이라면, num은 10
  for n in str(num):        #10을 문자열로 변환하면, n은 1과 0이 될 수 있다
    num += int(n)           #10에 1을 더하고 또 0을 더한다, 이 값은 생성자
  if num <= 10000:
    remove_list.append(num) #생성자를 제거 하기 위해 list에 넣는다.

for remove_num in set(remove_list): #set으로 중복값 제거
    numbers.remove(remove_num)  #
for self_num in numbers:
  print(self_num)    