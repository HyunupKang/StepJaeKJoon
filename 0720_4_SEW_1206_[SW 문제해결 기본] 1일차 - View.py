for test_case in range(1, 11):
    N = int(input())
    List = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        for f in range(List[i], 0, -1):
            if  f > List[i-1] and f > List[i-2] and f > List[i+1] and f > List[i+2]:
                result +=1
    print(f"#{test_case} {result}")