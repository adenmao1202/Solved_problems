# Try and Except
""" 
error order:
ZeroDevisionError -> ValueError -> IndexError.
""" 

def division(a, b):
    try:
        a = int(a)
        b = int(b)
        return float(a / b)
    
    except ZeroDivisionError:
        return "Division by zero"
    except ValueError:
        return "Invalid value"
        
   
def main(): 
    lis = input().split() # list of str 
    # print(lis)
    while True:
        try:
            input_index = input().split() # str
            first, second = int(input_index[0]), int(input_index[1]) # int 
            # print(first, second)
            
            # if len(input_index) != 2:
            #     raise IndexError
            #     continue
            
            if first > (len(lis) - 1) or second > (len(lis) - 1) or first < 0 or second < 0:
                raise IndexError
                continue
            
            nom, denom = lis[first], lis[second] # str of int or char 
            
            if not nom.isdigit() or not denom.isdigit():
                raise ValueError
                continue
            
            
            result = division(nom, denom) #str of int
            print(result)
            
        # order matters 
        except ZeroDivisionError:
            print("Division by zero")
        except ValueError:
            print("Invalid value")
        except IndexError:
            print("Index out of range")
        except EOFError:
            break
    
    
if __name__ == "__main__":
    main()