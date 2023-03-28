def merge_sorted_arrays(array_one, array_two) -> list:
    sorted_list = list()
    for item in array_one:
        sorted_list.append(item)

    for element in array_two:
        sorted_list.append(element)

    sorted_list.sort()

    return sorted_list


if __name__ == '__main__':
    array_one = [0, 3, 4, 31]
    array_two = [4, 6, 30]
    print(merge_sorted_arrays(array_one, array_two))
