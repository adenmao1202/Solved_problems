from fig08_04 import UG
from fig08_04 import Grad
from fig08_05 import Grades

# from fig08_08 import Grades


# Figure 8.6 : 這個是 --> 主程式
def gradeReport(course):
    """Assumes course is of type Grades"""

    report = ""  # 設定為空字串
    for s in course.getStudents(): # 寫兩層是因問每個學生有多筆成績
        tot = 0.0
        numGrades = 0  # 總共有幾筆成績
        for g in course.getGrades(s):
            tot = tot + g
            numGrades += 1
        try:
            average = tot / numGrades
            report = report + "\n" + str(s) + "'s mean grade is " + str(average)
        except ZeroDivisionError: # ValueError 
            report = report + "\n" + str(s) + " has no grades"
    return report


if __name__ == "__main__":
    # Humans
    # UG: IDNum 排序會按照創立物件的順序
    ug1 = UG("Jane Doe", 2014)
    ug2 = UG("John Dick", 2015)
    ug3 = UG("David Henry", 2003)
    # Grad
    g1 = Grad("Billy Buckner")
    g2 = Grad("Bucky F. Dent")

    # Get Grades : from fig 8.5
    CPPy = Grades()  # 實體化 Grades 這個 class
    CPPy.addStudent(ug1)
    CPPy.addStudent(ug2)
    CPPy.addStudent(g1)
    CPPy.addStudent(g2)

    for s in CPPy.getStudents():
        CPPy.addGrade(s, 75)  # 平均來說，所有：s 拿了 75

    #  加入額外分數
    CPPy.addGrade(g1, 25)
    CPPy.addGrade(g2, 100)

    CPPy.addStudent(ug3)  # Didn't assgined 75
    print(gradeReport(CPPy))
