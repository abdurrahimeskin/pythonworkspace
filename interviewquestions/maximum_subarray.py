def max_subarray(nums) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    total = 0
    maximum_value = nums[0]
    for i in range(len(nums)):
        # step 1 -> add the value to check
        total += nums[i]
        # step 2 -> choose the higher one
        maximum_value = max(maximum_value, total)
        # step 3 -> if current sum is lower than 0, make it 0
        if total < 0:
            total = 0
    return maximum_value


if __name__ == '__main__':
    nums_test_one = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums_test_two = [5, 4, -1, 7, 8]
    print(max_subarray(nums_test_one))
    print(max_subarray(nums_test_two))