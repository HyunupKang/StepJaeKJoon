import sys

n = int(sys.stdin.readline())
list = []


for i in range(n):
    temp = input()

    if (len(temp), temp) not in list:  # <-----몰랐던 기법, 이 문으로 중복은 제외함
        list.append((len(temp), temp))

answer = sorted(list, key=lambda x: (x[0], x[1]))

for ans in answer:
    print(ans[1])
