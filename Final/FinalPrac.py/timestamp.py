"""
Your task is to write a program that can store key-value pairs and 
retrieve the value associated with a given key. If a key is not found, return "nil".

Input
The input consists of multiple lines of commands.
Each command will be either a put command to store a value or a get command to retrieve a value.

put key value: Stores the value associated with the key.

get key: Retrieves the value associated with the key.
--------------------------------------------
Output
For each get command, output the value associated with the key. If the key is not found, output "nil".
"""
class simpleHash:
    def __init__(self):
        self.data = {}
        
    def put(self, key:str, value:str):
        self.data[key] = value
        
    def get(self, key):
        if key not in self.data:
            return "nil"
        return self.data[key]
    
def main():
    obj = simpleHash() # 實體化
    while True:
        try: 
            command = input().split() # list of str 
            if command[0] != "" and command[1] != "":
                if command[0] == "put":
                    key, value = command[1], command[2]
                    obj.put(key, value)
                    
                elif command[0] == "get":
                    key = command[1]
                    print(obj.get(key))

            else:
                raise EOFError
            
        except EOFError:
            break
        
if __name__ == "__main__":
    main()