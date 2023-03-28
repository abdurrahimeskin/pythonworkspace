
##O(n^2)
def common_elements(array_one, array_two) -> bool:
    for i in range(len(array_one)):
        if array_one[i] in array_two:
            return True
    return False


# O(n)
def common_elements_alternative(array_one, array_two) -> bool:
    hash_table = dict()
    for item in array_one:
        if item not in hash_table:
            hash_table[item] = True
    for element in array_two:
        if hash_table.get(element):
            return True
    return False


def common_elements_alternative_two(arr_one, arr_two) -> bool:
    output = [item for item in arr_one if item in arr_two]
    if len(output) > 0:
        return True
    return False


if __name__ == '__main__':
    array_one = ['a', 1, 'c', 'x']
    array_two = ['z', 1, 't']
    print(common_elements_alternative_two(array_one, array_two))
