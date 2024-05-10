# def gcd(a, b):  # a<b
#     while a != 0:
#         a, b = b % a, a  # small on the left, large on the right
#     return b


# a, b = input().split()
# input_a = a
# input_b = b
# if input_a == " " or input_b == " ":
#     print(" ")
# else:
#     a = int(input_a)
#     b = int(input_b)
#     print(gcd(a, b))


def gcd(a, b):  # a<b
    while a != 0:
        a, b = b % a, a  # small on the left, large on the right
    return b


input_str = input().split(",")
if len(input_str) == 0:
    print()
elif len(input_str) == 1:
    print()
else:
    a = int(input_str[0])
    b = int(input_str[1])
    print(gcd(a, b))
