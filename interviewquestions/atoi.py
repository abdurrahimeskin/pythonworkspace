def atoi(string):
    sign = 1
    i = 0
    n = len(string)
    num = 0

    if n == 0:
        return -1
    if string[0] == '+':
        i += 1
    elif string[0] == '-':
        sign = -1
        i += 1
    while i < n and string[i].isdigit():
        num = num * 10 + int(string[i])
        i += 1
    if i < n:
        return -1

    return sign * num


print(atoi("123"))  # Output: 123
print(atoi("-456"))  # Output: -456
print(atoi("+789"))  # Output: 789
print(atoi("  42"))  # Output: -1
print(atoi("2  23"))  # Output: -1
print(atoi("hello"))  # Output: -1
print(atoi(""))  # Output: -1
