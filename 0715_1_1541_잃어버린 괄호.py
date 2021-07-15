a = input().split('-')
result = 0
num_list = []
final = 0
for n in a:
    temp = n.split('+')
    for i in temp:
        result += int(i)
    num_list.append(result)
    result = 0

for n in range(len(num_list)):
    if n == 0:
        final += int(num_list[n])
    else:
        final -= int(num_list[n])

print(final)

# 41+73-72+0036-42+54+67 입력했다면
# ['41+73', '72+36', '42+54+67']로 만들고
# 첫번째 인덱스를 ['41','73']로 만든다음 덧셈 계산, 다른 인덱스도 마찬가지, 그러면
# ['114', '108', '163']이 됨
# 위 리스트를 -= 해주면 결과
