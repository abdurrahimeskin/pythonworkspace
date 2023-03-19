import string


def searching_challenge(str, token) -> string:
    words = str.split()
    count_list = list()
    for word in words:
        count = 1
        for i in range(0, len(word)):
            for j in range(i+1, len(word)):
                if word[i] == word[j]:
                    count = count+1
        count_list.append(count)

    if max(count_list) == 1:
        return -1
    else:
        indice_list = [index for index, item in enumerate(count_list) if item == max(count_list)]

    return words[min(indice_list)]


if __name__ == '__main__':
    print(searching_challenge("No words", "qstn4py"))
