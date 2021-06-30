def pibonacci(N):
    if N <= 1:
        return N
    return pibonacci(N-1) + pibonacci(N-2)


N = int(input())
print(pibonacci(N))


# 단순하게 N이면 N-1 결과와 N-2의 결과의 합과 같다.