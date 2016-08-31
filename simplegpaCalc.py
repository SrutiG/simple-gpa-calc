from tkinter import *
import college

class gpaCalcGUI():

    Semesters = []


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
        self.semesterWindows = []
        for x in range(numSemesters):
            semesterWin = Toplevel()
            semesterWin.withdraw()
            self.semesterWindows.append(semesterWin)
        self.semesterWindows.append(0)
        self.semesterWindows[0].deiconify()
        for number in range(len(self.semesterWindows)):
            self.enterSemesterInfo(self.semesterWindows[number], number+1)           

    def showWindow(self, prevWindow, nextWindow):
        if nextWindow != 0:
            prevWindow.withdraw()
            nextWindow.deiconify()
        else:
            prevWindow.withdraw()
            self.showGPA()

    def showGPA(self):
        mainWin = Tk()
        mainWin.title("Welcome")
        mainCollege = college.College(self.Semesters)
        gpa = mainCollege.gpa
        gpaLbl = Label(mainWin, text="your GPA is %s"%gpa)
        gpaLbl.grid(row=0)
        
    def enterSemesterInfo(self, root, semesterNum):
        classesLbl = Label(root, text="How many classes did you take in semester %d?" %semesterNum)
        classesLbl.grid(row = 0, columnspan = 3)
        classesEty = Entry(root, width = 5)
        classesEty.grid(row = 0, column = 4)
        enterBtn = Button(root, text="Enter", command = lambda:self.enterClassInfo(root, int(classesEty.get()), semesterNum))
        enterBtn.grid(row = 1, column=5)
        

    def enterClassInfo(self, semesterWin, numClasses, semesterNum):
        classesWin = Toplevel()
        credsLbl = Label(classesWin, text="Grade")
        credsLbl.grid(row= 0, column=1)
        gradeLbl = Label(classesWin, text="Credits")
        gradeLbl.grid(row= 0, column=2)
        gradeEtys = []
        credEtys = []
        for x in range(numClasses):
            rownum = x + 1
            classnumLbl = Label(classesWin, text="Class %d" %(x+1))
            classnumLbl.grid(row = rownum)
            gradeEty = Entry(classesWin, width=5)
            gradeEty.grid(row = rownum, column=1)
            credEty = Entry(classesWin, width = 5)
            credEty.grid(row = rownum, column=2)
            gradeEtys.append(gradeEty)
            credEtys.append(credEty)
        enterBtn = Button(classesWin, text="Enter", command = lambda:self.combineFuncs(self.semesterWindows[semesterNum-1], self.semesterWindows[semesterNum], semesterWin, classesWin, gradeEtys, credEtys))
        enterBtn.grid(row = numClasses+1)
        
    def combineFuncs(self, window1, window2, semesterWin, classesWin, gradeEtys, credEtys):
        self.enterData(semesterWin, classesWin, gradeEtys, credEtys)
        self.showWindow(window1, window2)

    def enterData(self, semesterWin, classesWin, gradeEtys, credEtys):
        classesWin.withdraw()
        semesterWin.withdraw()
        classes = []
        for x in range(len(gradeEtys)):
            grade = gradeEtys[x].get()
            cred = credEtys[x].get()
            newClass = college.Class(cred, grade)
            classes.append(newClass)
        newSemester = college.Semester(classes)
        self.Semesters.append(newSemester)

            
            

newWin = Tk()
loop = gpaCalcGUI(newWin)
newWin.mainloop()           
