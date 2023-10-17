import tkinter
from tkinter import ttk
from tkinter import messagebox

def EnterData():
    accepted = acceptVar.get()
    
    if accepted == "Accepted":
        
        firstName = firstEntry.get()
        lastName = lastEntry.get()
        
        if firstName and lastName:
            
            title = titleCombobox.get()
            ageLabel = ageSpinbox.get()
            nationalityLabel = nationCombo.get()
    
            numCourse = numSpinbox.get()
            numSems = numsSpinbox.get()
            registration = regStatus.get()
    
            print("First Name:", firstName, " ", "Last Name:", lastName)
            print("Title:", title, " ", "Age:", ageLabel, " ", "Nationality:", nationalityLabel)
            print("Number of Courses:", numCourse, " ", "Number of Semesters:", numSems)
            print("Registration Status:", registration)
            
        else:
            tkinter.messagebox.showwarning(title = "Error", message = "First Name and Last Name Required")
        
    else:
        tkinter.messagebox.showwarning(title = "Error", message = "Terms not yet accepted !!!")

window = tkinter.Tk()
window.title("Data Entry Form")
#window.configure()

frame = tkinter.Frame(window, bg = "#999966")
frame.pack()

userInfo = tkinter.LabelFrame(frame, text = "User Information", bg = "#999966")
userInfo.grid(row = 0, column = 0, padx = 20, pady = 10)

firstName = tkinter.Label(userInfo, text = "First Name", bg = "#999966")
firstName.grid(row = 0, column = 0)

lastName = tkinter.Label(userInfo, text = "Last Name", bg = "#999966")
lastName.grid(row = 0, column = 1)

firstEntry = tkinter.Entry(userInfo)
lastEntry = tkinter.Entry(userInfo)
firstEntry.grid(row = 1, column = 0)
lastEntry.grid(row = 1, column = 1)

title = tkinter.Label(userInfo, text = "Title", bg = "#999966")
titleCombobox = ttk.Combobox(userInfo, values = ["Mr.", "Ms.", "Mrs.", "Dr."])
title.grid(row=0, column=2)
titleCombobox.grid(row=1, column=2)

ageLabel = tkinter.Label(userInfo, text="Age", bg = "#999966")
ageSpinbox = tkinter.Spinbox(userInfo, from_ = 0, to = 99)
ageLabel.grid(row=2, column=0)
ageSpinbox.grid(row=3, column=0)

nationalityLabel = tkinter.Label(userInfo, text = "Nationality", bg = "#999966")
nationCombo = ttk.Combobox(userInfo, values = ["Nigeria", "Ghana", "Senegal", "Morocco", "Cameroon"])
nationalityLabel.grid(row=2, column=1)
nationCombo.grid(row=3, column=1)

for widget in userInfo.winfo_children():
    widget.grid_configure(padx = 9, pady = 5)
    
courseInfo = tkinter.LabelFrame(frame, text = "Course Info", bg = "#999966")
courseInfo.grid(row = 1, column=0, sticky="news", padx = 20, pady = 10)

registeredLabel = tkinter.Label(courseInfo, text="Registration Status", bg = "#999966")
regStatus = tkinter.StringVar(value = "Not Registered")
registerCheck = tkinter.Checkbutton(courseInfo, text="Currently Registered", variable = regStatus, onvalue="Registered", offvalue="Not Registered")
registeredLabel.grid(row=1, column=0)
registerCheck.grid(row=2, column=0)

numCourse = tkinter.Label(courseInfo, text = "Courses Registered", bg = "#999966")
numSpinbox = tkinter.Spinbox(courseInfo, from_ = 2, to = 12)
numCourse.grid(row = 1, column = 2)
numSpinbox.grid(row =2, column = 2)

numSems = tkinter.Label(courseInfo, text = "Number of Semesters", bg = "#999966")
numsSpinbox = tkinter.Spinbox(courseInfo, from_ = 1, to = 10)
numSems.grid(row = 1, column = 3)
numsSpinbox.grid(row = 2, column = 3)

for widget in courseInfo.winfo_children():
    widget.grid_configure(padx = 9, pady = 5)
    
termsFrame = tkinter.LabelFrame(frame, text = "Terms and Conditions", bg = "#999966")
termsFrame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)

acceptVar = tkinter.StringVar(value = "Not Accepted")
termsCheck = tkinter.Checkbutton(termsFrame, text = "Terms and Conditions Accepted", variable = acceptVar, onvalue = "Accepted", offvalue = "Not Accepted")
termsCheck.grid(row = 0, column = 0)

button = tkinter.Button(frame, text = "Enter Data", command = EnterData, bg = "#999966")
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)

window.mainloop()