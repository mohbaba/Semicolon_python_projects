# def count_characters(sample_input: str):
#     word = sample_input .lower()
#     letters = 0
#     digits = 0
#
#     for char in word:
#         if char in "abcdefghijklmnopqrstuvwxyz":
#             letters += 1
#         if char in "0123456789":
#             digits += 1
#     return f"LETTERS {letters} DIGITS {digits}"

def count_char(input):
    letters = 0
    digits = 0
    for char in input:
        if char.isalpha():
            letters += 1
        if char.isdigit():
            digits += 1
    return f"LETTERS {letters} DIGITS {digits}"

def count_cases(input):
    uppercase = 0
    lowercase = 0
    for char in input:
        if char.isupper():
            uppercase += 1
        if char.islower():
            lowercase += 1
    return f"UPPER CASE {uppercase} LOWER CASE {lowercase}"

# def count_cases(sample_input: str):
#     uppercase = 0
#     lowercase = 0
#
#     for char in sample_input:
#         if char in "abcdefghijklmnopqrstuvwxyz".upper():
#             uppercase += 1
#         if char in "abcdefghijklmnopqrstuvwxyz":
#             lowercase += 1
#     return f"UPPER CASE {uppercase} LOWER CASE {lowercase}"
