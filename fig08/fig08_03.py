# Figure 8.3
import datetime


class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(" ")
            
            self.lastName = name[lastBlank + 1 :]
        except:  # except ValueError from name withou space, that was assumed by lastBlank
            self.lastName = name
        self.birthday = None

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return f"name: {self.name}, birthdate: {self.birthday} "


class MITPerson(Person):
    nextIdNum = 0  # class variable：用來保證 id 的唯一性

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum


if __name__ == "__main__":
    p1 = MITPerson("Barbara Beaver")
    p1.setBirthday(datetime.date(1776, 7, 16))
    print(p1)
    # p1 = MITPerson("Barbara Beaver")
    # print(str(p1) + "'s id number is " + str(p1.getIdNum()))

    # p1 = MITPerson("Mark Guttag")
    # p2 = MITPerson("Billy Bob Beaver")
    # p3 = MITPerson("Billy Bob Beaver")
    # p4 = Person("Billy Bob Beaver")

    # print(p1)
    # print(p2)
    # print(p3)
    # print(p4)

    # print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
    # print(str(p2) + '\'s id number is ' + str(p2.getIdNum()))
    # print(str(p3) + '\'s id number is ' + str(p3.getIdNum()))
    # print(str(p4) + '\'s id number is ' + str(p4.getIdNum())) # error

    # print('p1 < p2 =', p1 < p2)
    # print('p3 < p2 =', p3 < p2)
    # print('p4 < p1 =', p4 < p1)
    # print('p1 < p4 =', p1 < p4) # error
