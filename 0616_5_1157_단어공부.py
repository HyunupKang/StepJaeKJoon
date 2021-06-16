words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])

# words가 hiiesqii -> HIIESQII이면
# unique_words는 HIESQ
# 반복문 첫 루틴이라면, words에서 H 갯수 count한 값이 cnt, 여기선 1
# 1을 cnt_list에 append

# cnt_list에서 가장 max값을 count함. 그런데 1이면 중복도가 같으니 ? 출력
# 1보다 크다면 cnt_list의 인덱스를 max_index 변수에 삽입
# max_index에 해당하는 unique_words 출력