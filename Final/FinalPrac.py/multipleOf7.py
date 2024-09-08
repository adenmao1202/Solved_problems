""" 
Write a function to determine if a given number is a multiple of 7. 
The rule to check if a number is a multiple of 7 is as follows:

Remove the last digit from the number, double it, and subtract it from the remaining number.
Repeat the process until a small number is obtained.
If the resulting number is a multiple of 7, then the original number is also a multiple of 7.
""" 
def multipleOf7(n):
    str_n = str(n)
    len_n = len(str_n)
    
    while len_n > 2: 
        last_digit = int(str_n[-1])
        remaining = int(str_n[:-1])
        
        if remaining > last_digit * 2:
            new_num = remaining - last_digit * 2
            str_n = str(new_num)
        else:
            break
        
    if int(str_n) % 7 == 0:
        return f"{n} is a multiple of 7."
    else:
        return f"{n} is not a multiple of 7."
        
    
def main():
    while True: 
        n = input()
        if int(n) != 0: 
            print(multipleOf7(n))
        else:
            break
    
if __name__ == "__main__":
    main()