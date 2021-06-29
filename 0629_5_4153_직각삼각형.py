while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    max_num = max(nums)
    nums.remove(max_num)

    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')
# 입력을 리스트로 받고,
# 리스트 중에서 가장 큰 값을 대변
# 그리고 리스트에 그 값을 제거
# 나머지 요소들로 공식 사용