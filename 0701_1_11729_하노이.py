def hanoi(cnt, first, third, second):
    start = first
    end = third
    mid = second
    if cnt == 1:
        print(start, end)
        return
    hanoi(cnt-1, start, mid, end)
    print(start, end)
    hanoi(cnt-1, mid, end, start)

n = int(input())
while True:
    sum = 2**n -1
    print(sum)
    hanoi(n, 1, 3, 2)
    break

# https://www.youtube.com/watch?v=FYCGV6F1NuY
#hanoi(원반 개수, 시작, 목표, 보조)
#hanoi(원반 개수 -1, 시작, 보조, 목표)
#print(시작, '->', 목표)  가장 큰 원반을 목표 기둥에 꽂음
#이후엔 n-1개
#hanoi(원반개수-1, 보조, 목표, 시작)보조기둥에 남은 원반이 다 쌓여있으니, 보조기둥이 시작기둥, 시작기둥은 보조 기둥임