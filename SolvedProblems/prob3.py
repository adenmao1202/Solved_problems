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


def iterate_string(s):
    """(n0​+n1​∗8+n2​∗7+n3​∗6+n4​∗5+n5​∗4+n6​∗3+n7​∗2+n8​∗1+n9​∗1)mod10=0"""

    total_sum = 0
    for i in range(1, len(s)):
        total_sum += int(s[i]) * (9 - i)
        if i == 8:
            break
    return total_sum


while True:
    try:
        rept_input = input()
        if rept_input.strip() == "":
            break

        else:
            rept = int(rept_input)

            for times in range(rept):
                string = input()
                if len(string) != 10:
                    print("Invalid")
                    continue
                elif not isinstance(string[0], str):  # elif string[0].isalpha():
                    print("Invalid")
                    continue
                elif string[1] == "1" or string[1] == "2":
                    final_sum = (
                        iterate_string(string)
                        + letter_to_int(string[0])
                        + int(string[9])
                    )
                    if final_sum % 10 == 0:
                        print("Valid")

                    else:
                        print("Invalid")
                else:
                    print("Invalid")
    except EOFError:
        break
