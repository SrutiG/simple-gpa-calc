'''
College
@author Sruti Guhathakurta


~~Future Updates~~
Previous Class/Semester and Current Class/Semester?
'''

'''
A Class object is initialized by giving the number of credits and the letter grade
it can be renamed. The GPA dictionary has keys which are strings of capital letters
and the corresponding GPA float value.
'''

class Class():

    gpaDict = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}

    '''
    Initializes the class and converts the letter grade to a float
    value and stores it in the grade variable
    @param creds: the number of credits
    @param letterGrade: the letter grade received in the class
    '''

    def __init__(self, creds, letterGrade):
        self.credits = creds
        self.letterGrade = letterGrade
        self.grade = self.gpaDict[self.letterGrade]

    '''
    Allows the addition of a name attribute to the Class
    @param name: the name of the class
    '''
    
    def nameClass(self, name):
        self.name = name

'''
A Semester object is initialized by passing in an array of classes.
It prompts the calculate GPA function on initialization
'''

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

'''
A College object is initialized by passing in an array of semesters.
It prompts the calculate GPA function on initialization
'''

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
