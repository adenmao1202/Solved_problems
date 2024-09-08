def letter_to_int(c):
    # Define the list of integers corresponding to letters A-Z
    num_list = [
        1,
        0,
        9,
        8,
        7,
        6,
        5,
        4,
        9,
        3,
        2,
        2,
        1,
        0,
        8,
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        1,
        3,
        2,
        0,
    ]
    # Convert the letter to an index (0-25) and return the corresponding integer
    return num_list[ord(c) - ord("A")]


# iteration
def iterate_process(Flist):
    total_sum = 0
    for i, num in enumerate(Flist[1:], start=1):
        result = int(num) * (9 - i)
        total_sum += result
        if i == 8:
            break
    return total_sum


# Main
while True:
    try:
        string = input()
        if len(string) != 10:
            continue
        n1 = int(string[1])
        if n1 != 1 and n1 != 2:
            print("Invalid")
            continue

        Flist = [x for x in string]
        n9 = string[9]
        Total = int(letter_to_int(Flist[0])) + int(n9) + int(iterate_process(Flist))

        if Total % 10 == 0:
            print("Valid")
        else:
            print("Invalid")

    except EOFError:
        break

# def letter_to_int(c):
#     # Define the list of integers corresponding to letters A-Z
#     num_list = [
#         1,
#         0,
#         9,
#         8,
#         7,
#         6,
#         5,
#         4,
#         9,
#         3,
#         2,
#         2,
#         1,
#         0,
#         8,
#         9,
#         8,
#         7,
#         6,
#         5,
#         4,
#         3,
#         1,
#         3,
#         2,
#         0,
#     ]

#     return num_list[ord(c) - ord("A")]


# def is_valid_id(id_str):
#     first_letter = id_str[0]
#     gender_digit = int(id_str[1])
#     rest_digits = list(map(int, id_str[2:]))

#     first_value = letter_to_int(first_letter)

#     if gender_digit != 1 and gender_digit != 2:
#         return "Invalid"

#     checksum = (
#         first_value + sum((i * (10 - idx)) for idx, i in enumerate(rest_digits))
#     ) % 10

#     if checksum == 0:
#         return "Valid"
#     else:
#         return "Invalid"


# # Main
# num_ids = int(input())

# all_results_printed = False

# for _ in range(num_ids):
#     id_input = input().strip()
#     result = is_valid_id(id_input)
#     print(result)

#     if _ == num_ids - 1:
#         all_results_printed = True

# if all_results_printed:
#     pass
