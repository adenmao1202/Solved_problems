# Figure 8.4

from fig08_03 import Person
from fig08_03 import MITPerson


class Student(MITPerson): # 繼承於 MITPerson
    
    def isStudent(self):                                               # isStudent is here!!
        return isinstance(self, Student)
        return type(self) == Grad or type(self) == UG


# 以下皆繼承於 Student, 因此都可以呼叫 isStudent()
class Grad(Student):
    pass


class UG(Student):  # 有加入classYear 這個 feauture
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class TransferStudent(Student):  # 有加入 fromSchool
    # it's a class
    # had nothing to do with grad and undergrad, since it's a transfer student
    # hence, open a new class

    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool  # 多出來的屬性

    def getOldSchool(self):
        return self.fromSchool


if __name__ == "__main__":
    p5 = Grad("Buzz Aldrin")
    p6 = UG("Billy Beaver", 1984)
    p3 = TransferStudent("Victor Tsai", "NCCU")

    print(p5, "is a graduate student is", type(p5) == Grad)
    print(p6, "is an undergraduate student is", type(p6) == UG)

    # All True since inheritance from MITPerson, which is also a type of student
    print(p5, "is a student is", p5.isStudent())
    print(p6, "is a student is", p6.isStudent())
    print(p3, "is a student is", p3.isStudent())
    # # Otherwise
    print(p3, "is a graduate student is", type(p3) == Grad)
    print(p3, "is an undergraduate student is", type(p3) == UG)
