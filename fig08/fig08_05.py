# Figure 8.5
class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}   # IDNum, grades 
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""

        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)  # list
        self.grades[student.getIdNum()] = []  # dict: key = IDNum, value = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""

        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError("Student not in mapping")

    def getGrades(self, student):  # return copy of list of student's grades
        """Return a list of grades for student"""
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError("Student not in mapping")

    def getStudents(self):  # return copy of list of students
        """Return a sorted list of the students in the grade book"""

        if not self.isSorted:  # 如果沒有排序過就排序
            self.students.sort()  # From MIT 裡面的 sort ()
            self.isSorted = True
        return self.students[:]
