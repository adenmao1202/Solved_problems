# Mod and Exception

def mod(a: str, b:str):
    try:
        return int(a) % int(b)
    
    except ZeroDivisionError:
        print("Division by zero")
        
    except ValueError:
        print("Invalid value")
        
        
        
def main():
    lis = input().split() # list of str
    print(lis)
    while True:
        try:
            index = input().split() # list of str
            if len(index) != 2:
                raise ValueError
                continue
            first_in = index[0] # str
            second_in = index[1] # str
            
            if int(first_in) > len(lis) -1  or int(second_in) > len(lis) -1:
                raise IndexError
                continue
            
            elif int(first_in) < 0 or int(second_in) < 0: #小於
                raise IndexError
                continue
            
            elif int(first_in) == int(second_in) == 0:
                raise EOFError
            
            else:
                nom = lis[int(index[0])] # str
                print(type(nom))
                denom = lis[int(index[1])] # str
                
                print(mod(nom, denom))
                
        except IndexError:
            print("Index out of range")
            
        except ValueError:
            print("Invalid value")  
            
        except EOFError:
            break
            
if __name__ == "__main__":
    main()