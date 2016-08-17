from tkinter import *

class gpaCalc():

    GPAdict = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    grades = []
    creds = []

    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")
        semesterLbl = Label(self.root, text="How many semesters have you completed?")
        semesterLbl.grid(row=0)
        self.semesterEty = Entry(self.root, width=5)
        self.semesterEty.grid(row=0, column=1)
        enterBtn = Button(self.root, text="Enter", command = self.helperFunction)
        enterBtn.grid(row=1)

    def helperFunction(self):
        self.root.withdraw()
        self.numSemesters = int(self.semesterEty.get())
        for x in range(self.numSemesters):
            self.enterSemesterInfo(x)
        self.calcGPA(grades, creds)
        self.showGPA()

    def enterSemesterInfo(self, semesterNum):
        self.semesterWin = Toplevel()
        classesLbl = Label(self.semesterWin, text="How many classes did you take in semester %d?" %(semesterNum+1))
        classesLbl.grid(row=0)
        self.classesEty = Entry(self.semesterWin, width = 5)
        self.classesEty.grid(row=0, column=1)
        enterBtn = Button(self.semesterWin, text="Enter", command = self.enterClassInfo)
        enterBtn.grid(row=1)

    def enterClassInfo(self):
        self.numClasses = int(self.classesEty.get())
        credsLbl = Label(self.semesterWin, text="Grade")
        credsLbl.grid(row=2, column=1)
        gradeLbl = Label(self.semesterWin, text="Credits")
        gradeLbl.grid(row=2, column=2)
        self.gradeEtys = []
        self.credEtys = []
        for x in range(self.numClasses):
            rownum = x + 3
            classnumLbl = Label(self.semesterWin, text="Class %d" %(x+1))
            classnumLbl.grid(rownum)
            gradeEty = Entry(self.semesterWin, width=5)
            gradeEty.grid(rownum, column=1)
            credEty = Entry(self.semesterWin, width = 5)
            credEty.grid(rownum, column=2)
            self.gradeEtys.append(gradeEty)
            self.credEtys.append(credEty)
        enterBtn = Button(self.semesterWin, text="Enter", command = self.enterData)
        enterBtn.grid(row=self.numClasses+3)

    def enterData(self):
        self.semesterWin.withdraw()
        for value in self.gradeEtys:
            grade = value.get()
            grades.append(GPAdict[grade])
        for item in self.credEtys:
            cred = item.get()
            creds.append(cred)
        
            

    def calcGPA(self, grade, cred):
        a = 0
        for x in range(len(grades)):
            a += grades[x] * creds[x]
        totalCreds = sum(creds)
        self.gpa = a/totalCreds
        self.gpaStr = "{0:.2f}".format(self.gpa)

    def showGPA(self):
        self.GPAWin = Toplevel()
        gpaLbl = Label(self.GPAWin, text="Your GPA is %s" %self.gpaStr)
        gpaLbl.grid(row=0)
        
        
newWin = Tk()
loop = gpaCalc(newWin)
newWin.mainloop()           
