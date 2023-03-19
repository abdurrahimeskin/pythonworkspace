def closestToZero(self, arr, n):
    arr.sort()  # sort the array in ascending order
    left, right = 0, n - 1
    min_sum = float('inf')

    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(min_sum):  # check if current sum is closer to zero than min_sum
            min_sum = current_sum
        if current_sum < 0:
            left += 1  # increment left index if current_sum is negative
        else:
            right -= 1  # decrement right index if current_sum is positive

    return min_sum

