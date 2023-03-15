def find_triplets(array, n) -> int:
    array.sort()

    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            sum_value = array[i] + array[left] + array[right]
            if sum_value == 0:
                return 1
            elif sum_value < 0:
                left += 1
            elif sum_value > 0:
                right -= 1
    return 0


if __name__ == '__main__':
    arr = [0, -1, 2, -3, 1]
    n = 5
    print(find_triplets(arr, n))
