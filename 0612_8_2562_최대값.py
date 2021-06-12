NumList = []
for i in range(9):
  NumList.append(int(input()))

print(max(NumList))
print(NumList.index(max(NumList))+1)

#append : 리스트에 요소 추가
#index(max()) : 맥스값의 인덱스 