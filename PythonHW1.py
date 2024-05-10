def temperature_conversion():

    temp = float(input())
    temp_type = input().upper().strip()

    if temp_type == "C":
        converted_temp = (9 / 5) * temp + 32
        print(f"The temperature is {round(converted_temp, 1)} F")
    elif temp_type == "F":
        converted_temp = (5 / 9) * (temp - 32)
        print(f"The temperature is {round(converted_temp, 1)} C")
    else:
        print("Invalid input")


temperature_conversion()
