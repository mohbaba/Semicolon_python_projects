def find_set(args):
    return set(args)


def sum_collection(user_input):
    total = 0
    for number in user_input:
        total += number

    return total


def remove_item(input_set: set, item: int) -> None:
    if item in input_set:
        input_set.remove(item)
    else:
        return None


def find_intersection(set1: set, set2: set) -> set:
    return set1.intersection(set2)


def generate_list() -> list:
    output_list = []
    for num in range(1, 16):
        output_list.append(num)

    return output_list


def duplicate_element(num_list: list) -> list:
    for number in range(len(num_list)):
        num_list.insert(number, num_list[number])
    return num_list
