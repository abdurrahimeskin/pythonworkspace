def first_unrepeated(arr) -> str:
    repeated = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                repeated.add(arr[i])

    unrepeated = [item for item in arr if item not in repeated]
    return unrepeated[0]


if __name__ == '__main__':
    array = ['x', 'y', 'z', 'y', 'x']
    print(first_unrepeated(array))
