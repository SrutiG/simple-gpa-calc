'''
College
Author: Sruti Guhathakurta


~~Future Updates~~
Previous Class/Semester and Current Class/Semester?
'''

'''
A Class object is initialized by giving the number of credits and the letter grade
it can be renamed. 

Attributes:
    gpaDict: The GPA dictionary has keys which are strings of capital letters
    and the corresponding GPA float value. 
'''

class Class():

    gpaDict = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}

    '''
    Initializes the class and converts the letter grade to a float
    value and stores it in the grade variable
    
    Args:
       creds: the number of credits
       letterGrade: the letter grade received in the class
    '''

    def __init__(self, creds, letterGrade):
        self.credits = creds
        self.letterGrade = letterGrade
        self.grade = self.gpaDict[self.letterGrade]

    '''
    Allows the addition of a name attribute to the Class
    
    Args:
       name: the name of the class
    '''
    
    def nameClass(self, name):
        self.name = name

'''
A Semester object is initialized by passing in an array of classes.
It prompts the calculate GPA function on initialization

Attributes:
    creds: an array of the credits of each class taken during the semester
    grades: an array of the numerical grade (4.0 scale) received in each class
'''

class Semester():

    creds = []
    grades = []

    '''
    Initializes the semester Object and sets the classArray and
    calls the calculateSemesterGPA function

    Args:
       classArray: an array of classes taken during the semester      
    '''

    def __init__(self, classArray):
        self.classArray = classArray
        self.calculateSemesterGPA()

    '''
    Calculates the Semester GPA by appending the credits and float grade
    to the creds and grades list, and multiplying the credits of a class
    with its corresponding grade and dividing it by the total number of credits.
    '''
    
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

Attributes:
    creds: array of the total number of credits taken in each semester
    grades: array of the average gpas from each semester
'''

class College():
    
    creds = []
    grades = []

    '''
    Initializes the College Object and sets the semesterArray and
    calls the calculateCollegeGPA function

    Args:
       semesterArray: an array of semester objects
    '''
    
    def __init__(self, semesterArray):
        self.semesterArray = semesterArray
        self.calculateCollegeGPA()

    '''
    Calculates the College GPA by using the individual Semester GPAs
    in the Semester array and adding up the total number of credits
    '''

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
