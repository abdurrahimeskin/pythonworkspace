def merge_sorted_arrays(array_one, array_two) -> list:

    for item in array_two:
        array_one.append(item)
    array_one.sort()

    return array_one


if __name__ == '__main__':
    array_one = [0, 3, 4, 31]
    array_two = [4, 6, 30]
    print(merge_sorted_arrays(array_one, array_two))
