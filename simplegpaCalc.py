from tkinter import *
import college

class gpaCalcGUI():


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
        self.createSemesterWin(self.numSemesters)

    def createSemesterWin(self, numSemesters):
        for x in range(numSemesters):
            semesterWin = Toplevel()
            semesterg = SemesterGUI(semesterWin, x+1)
            semesterWin.mainloop

    def showGPA(self):
        self.GPAWin = Toplevel()
        gpaLbl = Label(self.GPAWin, text="Your GPA is %s" %self.gpaStr)
        gpaLbl.grid(row=0)
        
class SemesterGUI():


    def __init__(self, root, semesterNum):
        self.root = root
        self.semesterNum = semesterNum
        classesLbl = Label(self.root, text="How many classes did you take in semester %d?" %self.semesterNum)
        classesLbl.grid(row = 0, columnspan = 3)
        self.classesEty = Entry(self.root, width = 5)
        self.classesEty.grid(row = 0, column = 4)
        enterBtn = Button(self.root, text="Enter", command = self.enterClassInfo)
        enterBtn.grid(row = 1, column=5)

    def enterClassInfo(self):
        self.classes = Toplevel()
        self.numClasses = int(self.classesEty.get())
        credsLbl = Label(self.classes, text="Grade")
        credsLbl.grid(row= 0, column=1)
        gradeLbl = Label(self.classes, text="Credits")
        gradeLbl.grid(row= 0, column=2)
        self.gradeEtys = []
        self.credEtys = []
        for x in range(self.numClasses):
            rownum = x + 1
            classnumLbl = Label(self.classes, text="Class %d" %(x+1))
            classnumLbl.grid(row = rownum)
            gradeEty = Entry(self.classes, width=5)
            gradeEty.grid(row = rownum, column=1)
            credEty = Entry(self.classes, width = 5)
            credEty.grid(row = rownum, column=2)
            self.gradeEtys.append(gradeEty)
            self.credEtys.append(credEty)
        enterBtn = Button(self.classes, text="Enter", command = self.enterData)
        enterBtn.grid(row = self.numClasses + 1)


    def enterData(self):
        self.classes.withdraw()
        self.root.withdraw()
        classes = []
        for x in range(len(self.gradeEtys)):
            grade = self.gradeEtys[x].get()
            cred = self.credEtys[x].get()
            newClass = college.Class(cred, grade)
            classes.append(newClass)
        self.newSemester = college.Semester(classes)
        return newSemester
            
            

newWin = Tk()
loop = gpaCalcGUI(newWin)
newWin.mainloop()           
