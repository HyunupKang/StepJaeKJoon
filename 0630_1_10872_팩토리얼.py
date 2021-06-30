def Factorial(N):
    result = 1
    if N > 0:
        result = N * Factorial(N-1)
    return result

N = int(input())
print(Factorial(N))