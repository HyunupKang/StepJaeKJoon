#0811_1_1713_후보 추천하기
'''
1. 추천 후보가 사진틀에 있으면 점수 +1
2. 새로운 후보가 추천 들어왔다면, 점수가 가장 낮은 후보들의 인덱스중 가장 첫번째 인덱스 가져오기
3. 그 인덱스에 해당하는 사진틀과 점수를 삭제
4. 새로운 후보를 사진틀과 점수에 append
'''
n = int(input())   # 사진틀 갯수
votetime = int(input())  # 전체 학생의 총 추천 횟수
recommend_student = list(map(int,input().split()))  # 추천 받은 학생
picture = []  # 사진틀
score = []

for i in recommend_student:
    if i in picture:
        indx = picture.index(i)
        score[indx] += 1
    else:
        if len(picture) >= n:
            idx = score.index(min(score)) # 오래된것 우선 빼는거니 앞에 있는 요소가 오래된거심
            del picture[idx]### <<<<<---------
            del score[idx]### <<<<<---------
        picture.append(i)
        score.append(1)

picture.sort()
print(' '.join(map(str,picture))) ### <<<<<---------