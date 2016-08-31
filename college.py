class Class():

    gpaDict = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}

    def __init__(self, creds, letterGrade):
        self.creds = creds
        self.letterGrade = letterGrade
        self.grade = self.gpaDict[self.letterGrade]

    def nameClass(name):
        self.name = name

class Semester():

    creds = []
    grades = []

    def __init__(self, classArray):
        self.classArray = classArray
        calculateSemesterGPA(self)

    def calculateSemesterGPA():
        credsxgrades = 0
        self.totalcreds = 0
        for x in self.classArray:
            creds.append(x.creds)
            grades.append(x.grade)
            credsxgrades = credsxgrades + x.creds*x.grade
            totalcreds = totalcreds + x.creds
        self.gpa = credsxgrades/totalcreds

        return self.gpa

class College():
    
    creds = []
    grades = []

    def __init__(self, semesterArray):
        self.semesterArray = semesterArray

    def calculateCollegeGPA(self):
        credsxgrades = 0
        totalcreds = 0
        for x in self.semesterArray:
            print(x)
            creds.append(x.totalcreds)
            grades.append(x.grade)
            credsxgrades = credsxgrades + x.creds*x.grade
            totalcreds = totalcreds + x.creds
        self.gpa = credsxgrades/totalcreds

        return self.gpa           
