import datetime
class Person(object): 

    def __init__(self, name, gpa, country):
        self.name = name 
        self.gpa = float(gpa)
        self.country = country
        
        try:
            self.lastName = name.split(" ")[-1]
        
        except:
            self.lastName = name

        self.birthday = None
        
    def get_country(self):
        return self.country
    
    def set_country(self, nation):
        self.country = nation
        
    def set_Gpa(self, newGpa):
        self.gpa = newGpa
    
    def Gpa_to_rank(self):
        if self.gpa >= 4:
            return "A"
        elif self.gpa >= 3.5: # elif 排除上面的
            return "B"
        elif self.gpa >= 3:
            return "C"
        elif self.gpa >= 2:
            return "D"
        else:
            return "F"
        
    def can_enter_master(self):
        if self.getAge() <= 23:
            if self.getGpa() >= 3:
                return True
            else:
                return False
        else:
            return False
        
    def exp_master_rank(self):
        if self.can_enter_master() == True:
            if self.getGpa() >= 4:
                return "top 10"
            elif self.getGpa() >= 3.5:
                return "top 20"
            else:
                return "top 50"
        else: 
            return "can't enter master"
        
    def set_birthday(self, birthdate):
        self.birthday = birthdate
        
    def getAge(self):
        if self.birthday == None:
            raise ValueError("please enter birthday first")
        else:
            return int((datetime.date.today() - self.birthday).days // 365)
    
    def sort_by_age(self):
        return sorted(all_interviewiees, key=lambda x: x.getAge())

    def __lt__(self, other): 
        
        if self.gpa < other.gpa:
            return True
        else:
            return False
        

    def __str__(self):
        return (f" Info: Name: {self.name}, Gpa: {self.gpa}, GpaRank: {self.Gpa_to_rank()}, "
                f" Country: {self.country}, Age: {self.getAge()}, ExpMaster: {self.exp_master_rank()}")

    def __repr__(self):
        return (f" Info: Name: {self.name}, Gpa: {self.gpa}, GpaRank: {self.Gpa_to_rank()}, "
                f" Country: {self.country}, Age: {self.getAge()}, ExpMaster: {self.exp_master_rank()}")

  
def execution():
    num_of_person = int(input("enter number of people: "))
    
    all_interviewiees = []
    
    for i in range(num_of_person):
        input_name = input("enter name: ").split(" ")
        input_gpa = float(input("enter gpa: "))
        input_country = input("enter nationality: ")
    
        person = Person(input_name, input_gpa, input_country)
        all_interviewiees.append(person)
        

    while True: 
        tick = input("Enter command or '---' to stop: ")
        if tick == "---":
            print(all_interviewiees)
            break
        else:
            
            command = input("enter command: ").split(", ")
            cmd = command[0]
            cat = command[1]
        
            if cmd == "sort":
                if cat == "gpa":
                    sortedList = sorted(all_interviewiees, key=lambda x: x.gpa)
                    print(sortedList)
                elif cat == "age":
                    sortedList = sorted(all_interviewiees, key=lambda x: x.getAge())  
                    print(sortedList)  
                else:
                    print("no such sorting method")
            
            else:
                print("no such command")
    
    
    
    
if __name__ == "__main__":
    execution()