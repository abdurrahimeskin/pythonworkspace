def twoSum(nums, target) -> list[int]:
    hash_table = dict()
    new_list = list()
    for i in range(len(nums)):
        hash_table[nums[i]] = i
    for item in nums:
        if hash_table.get(target - item) is not None and hash_table.get(target - item) != nums.index(item):
            new_list.append(nums.index(item))
            new_list.append(hash_table.get(target - item))
            break
    return new_list


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))
