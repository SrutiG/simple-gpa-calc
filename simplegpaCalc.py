'''
Simple GPA Calculator
@author Sruti Guhathakurta


~~Future Updates (in order)~~
-aesthetic improvements (fonts, font sizes, backgrounds...etc)
-creating an SQL database so that the user can save his/her info
-login window
-adding a button on the main window to add another semester (and updating the GPA accordingly)
-adding the option to enter class names
-having an option to display the classes already taken
-allowing the user to enter classes that will be taken in the future
-having a progress log where the user can see their current GPA,
  classes already completed, and classes left to complete
  and how they should perform in those classes to get their goal GPA
-having the user enter their university information and linking it to the University course catalog?
  this would allow the display of average GPAs (CourseCritique)
  Professor information
  Whether/not the course that the user is planning to take will be offered during a certain semester

@import tkinter
@import college.py
@import tkMessageBox
'''

from tkinter import *
import college

'''
A GUI that allows a user to enter the number of semesters they have completed,
the number of classes and the grades/credits for each class.
Calculates the GPA and displays it on the main window
'''

class gpaCalcGUI():

    Semesters = []
    
    '''
    Creates the initial window with title "GPA Calculator"
    which asks the user to input the number of semesters he/she has completed.
    the enter button prompts a helper function
    @param root: the Tk window used to display this information
    '''
    
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")
        semesterLbl = Label(self.root, text="How many semesters have you completed?")
        semesterLbl.grid(row=0)
        self.semesterEty = Entry(self.root, width=5)
        self.semesterEty.grid(row=0, column=1)
        enterBtn = Button(self.root, text="Enter", command = self.helperFunction)
        enterBtn.grid(row=0, column=2)

    '''
    Hides the main window and gets the number of semesters from the entry box
    prompts the createSemesterWin function to input the necessary info. Checks
    for valid input
    '''

    def helperFunction(self):
        self.root.withdraw()
        try:
            self.numSemesters = int(self.semesterEty.get())
            self.createSemesterWin(self.numSemesters)
        except Exception:
            self.errorFunc("Invalid Input- must be a number", self.root)

    '''
    creates an error window with a message that explains
    the type of error
    @param errorMessage: the message associated with the error
    '''

    def errorFunc(self, errorMessage, currentWin):
        errorWin = Toplevel()
        errorWin.title("Error!")
        errorLbl = Label(errorWin, text="%s"%errorMessage)
        errorLbl.grid(row=0)
        backBtn = Button(errorWin, text = "Back", command = lambda:self.withdrawErrorWin(errorWin))
        backBtn.grid(row=1)
        currentWin.deiconify()
        
    '''
    withdraws the error window
    @param window- the window to withdraw
    '''
    
    def withdrawErrorWin(self, window):
        window.withdraw()
    '''
    Uses the number of semesters inputted by the user to create the correct number
    of semester windows. Adds them to an array so that each can be accessed individually.
    and to prevent all of them from showing at once. Shows the first window and hides the rest.
    @param numSemesters: the number of semesters that the user has completed
    '''

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

    '''
    While the createSemesterWin function is looping through the number of semesters,
    it creates many Toplevels in the process. This ensures that the right one is being shown by
    withdrawing the previous and showing the next when the enter button on the classes window
    is clicked. If there are no more windows afterwards, it shows the main window.
    @param prevWindow: the previous window which already has the necessary data and needs to be hidden
    @param nextWindow: the next window which is blank for the user to input information
    '''

    def showWindow(self, prevWindow, nextWindow):
        if nextWindow != 0:
            prevWindow.withdraw()
            nextWindow.deiconify()
        else:
            prevWindow.withdraw()
            self.showGPA()

    '''
    creates the main window, sets the size to 250 by 250
    and creates a College object by using the semester array created by inputting the
    class data. The College object automatically calculates the GPA on initialization.
    A label with this information is created and centered on the window.
    '''

    def showGPA(self):
        mainWin = Tk()
        mainWin.title("Welcome")
        mainWin.geometry("250x250")
        mainCollege = college.College(self.Semesters)
        gpa = mainCollege.gpa
        gpaLbl = Label(mainWin, text="your GPA is {0:.2f}".format(gpa))
        gpaLbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    '''
    Creates the label, entry, and button for the semester window and sets the function
    of the button to create a new Toplevel to enter class information
    @param root: the window where all the information is displayed
    @param semesterNum: the number of the Semester that the window is displaying
    '''

    def enterSemesterInfo(self, root, semesterNum):
        classesLbl = Label(root, text="How many classes did you take in semester %d?" %semesterNum)
        classesLbl.grid(row = 0, columnspan = 3)
        classesEty = Entry(root, width = 5)
        classesEty.grid(row = 0, column = 4)
        enterBtn = Button(root, text="Enter", command = lambda:self.helperFunction2(root, classesEty, semesterNum))
        enterBtn.grid(row = 0, column=5)

    '''
    Helper function makes sure that the user input for number of classes
    is a valid number
    '''

    def helperFunction2(self, semesterWin, entry, semesterNum):
        try:
            self.enterClassInfo(semesterWin, int(entry.get()), semesterNum)
        except Exception:
            self.errorFunc("Invalid input- must be a number", semesterWin)

    '''       
    creates the necessary number of widgets to enter class information based on the user
    inputted number of classes taken in the semester. The enter button hides the windows used
    to enter info for the current semester and display the ones for the next semester.
    it also prompts the data entry function
    @param semesterWin the window that asked for the number of semesters
    @param numClasses the number of classes taken during the semester
    @param semesterNum the number of the semester
    '''

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
        enterBtn = Button(classesWin, text="Enter", width = 10,
                command = lambda:self.enterData(self.semesterWindows[semesterNum-1],
                self.semesterWindows[semesterNum], semesterWin, classesWin, gradeEtys, credEtys))
        enterBtn.grid(row = numClasses+1, column=1, columnspan=2)

    '''       
    This function uses the information the user inputted about the classes they took during the semester
    to create many class objects and store them in an array. This array is then used to create a semester object.
    The semester object is stored in the Semesters array.
    @param window1: the window of the classes data is being entered for
    @param window2: the next window to show
    @param semesterWin: the window to enter the number of classes in the semester
    @param classesWin: the window to enter the information about those classes
    @param gradeEtys: an array of the entries that have grades in them
    @param credEtys: an array of the entries that have credits stored in them
    '''

    def enterData(self, window1, window2, semesterWin, classesWin, gradeEtys, credEtys):
        classesWin.withdraw()
        semesterWin.withdraw()
        classes = []
        for x in range(len(gradeEtys)):
            grade = gradeEtys[x].get()
            cred = credEtys[x].get()
            try:
                newClass = college.Class(float(cred), grade)
                classes.append(newClass)
            except Exception:
                self.errorFunc("Grade must be A, B, C, D, or F; Credits must be a number", classesWin)
                return
        newSemester = college.Semester(classes)
        self.Semesters.append(newSemester)
        self.showWindow(window1, window2)

            
            

newWin = Tk()
loop = gpaCalcGUI(newWin)
newWin.mainloop()           
