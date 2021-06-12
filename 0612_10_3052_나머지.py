arr = []
for i in range(10):
  n = int(input())
  arr.append(n%42)

arr= set(arr)
print(len(arr))  


# set은 집합 자료형으로서, 중복을 제거하기 위한 필터 역할로 사용되고, 순서가 없음
# 그리고 len으로 arr 길이(길이가 인덱스 갯수 말하는 건가) 출력