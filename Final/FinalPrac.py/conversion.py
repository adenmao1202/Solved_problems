# unit conversion 
""" 
Problem: Unit Conversion
Description
We have different units of length: Inches (in), Feet (ft), Yards (yd), and Miles (mi). Here are their values relative to inches:

1 inch (in) = 1 inch
1 foot (ft) = 12 inches
1 yard (yd) = 36 inches
1 mile (mi) = 63,360 inches
For example, 5 feet is written as 5ft and is equal to 5 * 12 = 60 inches. Similarly, 3 yards is written as 3yd and is equal to 3 * 36 = 108 inches.

You will be given a string s representing a length measurement in one of the units mentioned above. You need to convert it into the equivalent length in inches.

Input
A string s representing a length measurement in one of the units (in, ft, yd, mi).
Output
An integer representing the equivalent length in inches.
The input length will be in the range of [1, 1,000,000] inches when converted.
""" 
def conversion(unit, num):
    if unit == "in":
        return num
    elif unit == "ft":
        return num * 12
    elif unit == "yd":
        return num * 36
    elif unit == "mi":
        return num * 63360    
# def conversion(unit, num):
#  conversion_factors = {
    #     "in": 1,
    #     "ft": 12,
    #     "yd": 36,
    #     "mi": 63360
    # }
    # return num * conversion_factors[unit]

def main():
    while True:
        try: 
            line = input().strip()  # removing trailing 
            if not line: 
                break
            unit = line[-2:]
            num = line[0:-2]
            
            if unit not in ["in", "ft", "yd", "mi"]:
                raise ValueError
            elif not num.isdigit():
                raise TypeError
            
            int_num = int(num)
            if int_num < 0 or int_num > 1000000:
                raise ValueError 
            print(conversion(unit, int_num))
        
        
        except TypeError:
            print("Invalid type")
        
        except ValueError:
            print("Invalid val")
            
        except EOFError:
            break
        
if __name__ == "__main__":
    main()
         
        