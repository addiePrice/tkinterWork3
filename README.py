from tkinter import *
import random

top = Tk()
groceryList = []
myRolls = []
rollTimes = []
dieType = []

def results():
    print(groceryList)
      
def exportList():
    with open('test.txt', 'w') as f:
        for item in groceryList:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs", bg = "#b2d8d8")
    LMain.grid(column = 2, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "#66b2b2", command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "#008080", command = week2)
    B2Main.grid(column = 2, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "#006666")
    B3Main.grid(column = 2, row = 4)

def week1():
    
    def addToList():
        newItem = E1.get()
        groceryList.append(newItem)
        E1.delete(0, END)

    clearWindow()
    
    #this is a Label widget
    L1 = Label(top, text = "Type stuff :)", bg = "#b2d8d8")
    L1.grid(column = 0, row = 1)

    #this is an Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #this is a Button widget
    B1 = Button(text = "   Print Stuff   ", bg = "#008080", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = "  +  ", bg = "#66b2b2", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "  Export Stuff  ", bg = "#006666", command = exportList)
    B3.grid(column = 0, row = 4)
    
    Bclear = Button(text = "Main Menu", bg = "white", command = mainMenu)
    Bclear.grid(column = 3, row = 1)

def week2():
    def rollDice():
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        clearWindow()

        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        L4W2 = Label(top, text = "Here are your results:", bg = "#b2d8d8")
        L4W2.grid(column = 2, row = 2)
        L5W2 = Label(top, text = "{}".format(myRolls), bg = "#66b2b2")
        L5W2.grid(column = 2, row = 3)
        B2W2 = Button(text = "Main Menu", bg = "white", command = mainMenu)
        B2W2.grid(column = 3, row = 0)

        
    clearWindow()
    L1W2 = Label(top, text="Dice Roller Program", bg = "#b2d8d8")
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text = "How many sides?", bg = "#66b2b2")
    L2W2.grid(column = 0, row = 2)
    
    L3W2 = Label(top, text = "How many rolls?", bg = "#66b2b2")
    L3W2.grid(column = 2, row = 2)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)
    
    B1W2 = Button(text = "Roll!", bg= "#008080", command = rollDice)
    B1W2.grid(column = 2, row = 4)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()

