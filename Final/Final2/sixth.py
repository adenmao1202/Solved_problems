"""
Description
Create a Python class called StudentRoster that manages student information for a course. 
Each student has a name and a student_id. 
The class should be able to add new students, remove students by student_id, and retrieve a student's information.
----
Input
The input will be given in the following format.
----
command student field [value]
There are three kinds of command.
---
add
e.g. add Mandy score 100
This will add a record of student Mandy have score 100.
---
remove
e.g. remove Mandy score
This will remove score record for Mandy
---
get
e.g. get Mandy score
This will retrieve Mandy's score

exit: stop the program
""" 
class StudentRoster:
    def __init__(self):
        self.data = {}
    
    def add(self, name, field, score):
        self.data[name] = score
    
    def remove(self, name):
        if name in self.data:
            del self.data[name]
    
    def get(self, name):
        return self.data[name]