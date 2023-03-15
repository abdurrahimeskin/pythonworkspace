def greater_element(arr, n):
    # Complete the function
    result = [1] * n
    for i in range(0, n):
        if arr[i] == max(arr):
            result[i] = -10000000
        else:
            filtered = [x for x in arr if x > arr[i]]
            filtered.sort()
            result[i] = filtered[0]
    return result


arr = [13, 6, 7, 12]
print(greater_element(arr, 4))
