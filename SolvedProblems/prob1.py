""" 
1. 兩個input
    1. temp: float 
    2. temp_type: str
        if, elif, else
3. 套公式
    Celsius to Fahrenheit: F = (9 / 5) * C + 32

    Fahrenheit to Celsius: C = (5 / 9) * (F - 32)
4. output:
    "The temperature is {temperature} {C or F}"
    If the character is neither 'C' nor 'F', please output "Invalid input"
"""


def temp_conv():
    temp = float(input())
    temp_type = input().upper().strip()  # upper() 轉大寫 strip() 去除空白

    if temp_type == "F":
        C_temp = (5 / 9) * (temp - 32)
        print(f"The temperature is {C_temp} C")
    elif temp_type == "C":
        F_temp = (9 / 5) * temp + 32
        print(f"The temperature is {F_temp} F")
    else:
        print("Invalid input")


if __name__ == "__main__":
    temp_conv()
