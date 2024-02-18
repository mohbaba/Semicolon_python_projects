def concatenate_swap(string1: str, string2: str) -> str:
    char_array = []
    new_string = ''
    for alphabet in string2:
        char_array.append(alphabet)
    char_array[-1] = string1[-1]
    char_array.append(' ')
    for alphabet in string1:
        char_array.append(alphabet)
    char_array[-1] = string2[-1]
    for element in char_array:
        new_string += element
    return new_string


def concatenate_swap1(string1: str, string2: str) -> str:
    return string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]
