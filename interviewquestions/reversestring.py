def reversestring(string) -> str:
    if len(string) == 0:
        return string
    else:
        return reversestring(string[1:]) + string[0]


def reversestring_alternative(string) -> str:
    return string[::-1]


if __name__ == '__main__':
    string = 'Abdurrahim'
    print(reversestring(string))
    print(reversestring_alternative(string))
