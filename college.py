class Class():

    gpaDict = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}

    def __init__(self, creds, letterGrade):
        self.credits = creds
        self.letterGrade = letterGrade
        self.grade = self.gpaDict[self.letterGrade]

    def nameClass(self, name):
        self.name = name

class Semester():

    creds = []
    grades = []

    def __init__(self, classArray):
        self.classArray = classArray
        self.calculateSemesterGPA()

    def calculateSemesterGPA(self):
        credsxgrades = 0
        self.totalcreds = 0
        for x in self.classArray:
            self.creds.append(x.credits)
            self.grades.append(x.grade)
            credsxgrades = credsxgrades + float(x.credits)*x.grade
            self.totalcreds = self.totalcreds + float(x.credits)
        self.gpa = credsxgrades/self.totalcreds

        return self.gpa

class College():
    
    creds = []
    grades = []

    def __init__(self, semesterArray):
        self.semesterArray = semesterArray
        self.calculateCollegeGPA()

    def calculateCollegeGPA(self):
        credsxgrades = 0
        self.totalcreds = 0
        for x in self.semesterArray:
            self.creds.append(x.totalcreds)
            self.grades.append(x.gpa)
        for x in range(len(self.creds)):
            credsxgrades = credsxgrades + self.creds[x]*self.grades[x]
        self.totalcreds = sum(self.creds)
        self.gpa = credsxgrades/self.totalcreds

        return self.gpa           
