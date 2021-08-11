#0810_1_8979_올림픽
'''
1. 금메달 많은 순으로 정렬, 금매달이 같다면 은, 은이 같다면 동, 내림차순
2. 국가번호의 index를 찾고, 정렬된 배열을 검사하며 국가번호 index의 금메달, 은, 동의 수가 같다면
3. i에 1을 더한 값을 출력
'''
# 국가 수, 등수를 알고 싶은 국가 
n, k = map(int, input().split())

medals = []
for i in range(n):    
    medals.append(list(map(int, input().split())))

medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

# k의 국가 인덱스 찾기
for i in range(n):
    if medals[i][0] == k:
        index = i

# 메달이 같은지 판별.
for i in range(n):
    if medals[index][1:] == medals[i][1:]:  # <<---- 이거 존나 테크닉 쩌네, 
        print(i+1)
        break
# 만약 정렬된 것이 [[1, 1, 2, 0], [2, 0, 1, 0], [3, 0, 1, 0], [4, 0, 0, 1]] 이고 k = 3일때
# i = 0 => false
# i = 1 => true  답은 2가 되고

# k = 2라 해도
# i = 0 => false
# i = 1 => true  답은 2가 됨