def get_highest_occurring(user_input: list):
    new_list = []
    count = 0
    number = 0
    for num in user_input:
        if count < user_input.count(num):
            count = user_input.count(num)
            number = num
    new_list.append(count)
    new_list.append(number)
    return new_list
