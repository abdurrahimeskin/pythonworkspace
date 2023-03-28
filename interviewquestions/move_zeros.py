def move_zeros(nums) -> list[int]:
    new_list = list()
    counter = 0
    if len(nums) <= 1:
        return nums

    for item in nums:
        if item != 0:
            new_list.append(item)
        else:
            counter += 1
    for i in range(counter):
        new_list.append(0)
    return new_list


def move_zeros_alternative(nums) -> list[int]:
    if len(nums) <= 1:
        return nums
    counter = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            counter += 1
    nums = [x for x in nums if x != 0]
    for i in range(counter):
        nums.append(0)
    return nums


def move_zeros_alternative_two(nums) -> list[int]:
    k = 0
    counter = 0
    for item in nums:
        if item != 0:
            nums[k] = item
            k += 1
    for i in range(k, len(nums)):
        nums[i] = 0
    return nums


if __name__ == '__main__':
    nums_one = [0, 1, 11, 0, 0, 0, 3, 12]
    nums_two = [0]
    nums_three = [0, 1, 0, 3, 12]
    print(move_zeros_alternative(nums_three))
    print(move_zeros(nums_three))
    print(move_zeros_alternative_two(nums_three))