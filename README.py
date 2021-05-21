from tkinter import *
import random
import numpy
import matplotlib.pyplot as plot

top = Tk()
groceryList = []
myRolls = []
rollTimes = []
dieType = []
myList = []

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
    LMain = Label(top, text = "Block 5 GUIs", bg = "#b2d8d8", font = ("Times", 11, "bold"))
    LMain.grid(column = 2, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "#66b2b2", font = ("Times", 11), command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "#008080", font = ("Times", 11), command = week2)
    B2Main.grid(column = 2, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "#006666", font = ("Times", 11), command = week3)
    B3Main.grid(column = 2, row = 4)

def week1():
    
    def addToList():
        newItem = E1.get()
        groceryList.append(newItem)
        E1.delete(0, END)

    clearWindow()
    
    #this is a Label widget
    L1 = Label(top, text = "Type stuff :)", bg = "#b2d8d8", font = ("Times", 11, "bold"))
    L1.grid(column = 0, row = 2)

    #this is an Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 3)

    #this is a Button widget
    B1 = Button(text = "   Print Stuff   ", bg = "#008080", font = ("Times", 11), command = results)
    B1.grid(column = 0, row = 4)

    B2 = Button(text = "  +  ", bg = "#66b2b2", font = ("Times", 11), command = addToList)
    B2.grid(column = 1, row = 3)

    B3 = Button(text = "  Export Stuff  ", bg = "#006666", font = ("Times", 11), command = exportList)
    B3.grid(column = 0, row = 5)
    
    Bclear = Button(text = "Main Menu", bg = "#ccece6", font = ("Times", 11), command = mainMenu)
    Bclear.grid(column = 3, row = 1)

def week2():
    def rollDice():
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        clearWindow()

        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        L4W2 = Label(top, text = "Here are your results:", bg = "#b2d8d8", font = ("Times", 11))
        L4W2.grid(column = 2, row = 2)
        L5W2 = Label(top, text = "{}".format(myRolls), bg = "#66b2b2", font = ("Times", 11))
        L5W2.grid(column = 2, row = 3)
        B2W2 = Button(text = "Main Menu", bg = "#ccece6", font = ("Times", 11), command = mainMenu)
        B2W2.grid(column = 3, row = 0)

        
    clearWindow()
    L1W2 = Label(top, text="Dice Roller Program", bg = "#b2d8d8", font = ("Times", 11, "bold"))
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text = "How many sides?", bg = "#66b2b2", font = ("Times", 11))
    L2W2.grid(column = 0, row = 2)
    
    L3W2 = Label(top, text = "How many rolls?", bg = "#66b2b2", font = ("Times", 11))
    L3W2.grid(column = 2, row = 2)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)
    
    B1W2 = Button(text = "Roll!", bg= "#008080", font = ("Times", 11), command = rollDice)
    B1W2.grid(column = 2, row = 4)

    Bclear2 = Button(text = "Main Menu", bg = "#ccece6", font = ("Times", 11), command = mainMenu)
    Bclear2.grid(column = 3, row = 1)

def week3():

    def addToList2():
        clearWindow()
        
        def addToList3():
            newItem2 = E1.get()
            myList.append (int(newItem2))
            E1.delete(0, END)
            print(myList)

        B1 = Button(text = "  +  ", bg = "#66b2b2", font = ("Times", 11), command = addToList3)
        B1.grid(column = 1, row = 3)

        L1 = Label(top, text = "What number?", bg = "#b2d8d8", font = ("Times", 11, "bold"))
        L1.grid(column = 0, row = 1)
            
        E1 = Entry(top, bd = 5)
        E1.grid(column = 0, row = 2)

        Bclear = Button(text = "Week 3", bg = "#ccece6", font = ("Times", 11), command = week3)
        Bclear.grid(column = 3, row = 1)

    def addABunch():
        clearWindow()
        
        def addaBunch2():
            numToAdd =  E1.get()
            numRange = E2.get()
            for x in range(0, int(numToAdd)):
                myList.append(random.randint(0, int(numRange)))
            print(myList)

        B1 = Button(text = "  +  ", bg = "#66b2b2", font = ("Times", 11), command = addaBunch2)
        B1.grid(column = 1, row = 3)

        L1 = Label(top, text = "How many numbers?", bg = "#b2d8d8", font = ("Times", 11, "bold"))
        L1.grid(column = 0, row = 1)

        E1 = Entry(top, bd = 5)
        E1.grid(column = 0, row = 2)
        
        L2 = Label(top, text = "How high should they go?", bg = "#b2d8d8", font = ("Times", 11, "bold"))
        L2.grid(column = 2, row = 1)

        E2 = Entry(top, bd = 5)
        E2.grid(column = 2, row = 2)
        
        Bclear = Button(text = "Week 3", bg = "#ccece6", font = ("Times", 11), command = week3)
        Bclear.grid(column = 3, row = 1)
        
    def searchList():
        clearWindow()
        def searchList2():
            searchItem = E1.get()
            indexCount = 0
            for x in range(len(myList)):
                if myList[x] == int(searchItem):
                    indexCount = indexCount + 1
                    print("Your item is #{} in the list".format(x + 1))
            print("Your item appeared {} times in the list".format(indexCount))

        B1 = Button(text = "Search", bg = "#66b2b2", font = ("Times", 11), command = searchList2)
        B1.grid(column = 1, row = 2)

        L1 = Label(top, text = "What Number?", bg = "#b2d8d8", font = ("Times", 11, "bold"))
        L1.grid(column = 0, row = 1)

        E1 = Entry(top, bd = 5)
        E1.grid(column = 0, row = 2)

        Bclear = Button(text = "Week 3", bg = "#ccece6", font = ("Times", 11), command = week3)
        Bclear.grid(column = 3, row = 1)

        
    def plotList():
        plot.scatter(myList, numpy.zeros_like(myList))
        plot.title('Your List :)')
        plot.yticks([])
        plot.show()



    def clearList():
        clearWindow()
        myList.clear()
        print(myList)
        L1W3 = Label(top, text = "Your list has been cleared.", bg = "#b2d8d8", font = ("Times", 11, "bold"))
        L1W3.grid(column = 1, row = 1)
        Bclear = Button(text = "Week 3", bg = "#ccece6", font = ("Times", 11), command = week3)
        Bclear.grid(column = 3, row = 1)

    clearWindow()
    
    L1W3 = Label(top, text = "List Program", bg = "#b2d8d8", font = ("Times", 11, "bold"))
    L1W3.grid(column = 0, row = 1)

    B1W3 = Button(text = "Add One Number", bg= "#b2d8d8", font = ("Times", 11), command = addToList2)
    B1W3.grid(column = 0, row = 4)

    B2W3 = Button(text = "Add a Bunch", bg= "#66b2b2", font = ("Times", 11), command = addABunch)
    B2W3.grid(column = 0, row = 5)

    B3W3 = Button(text = "Search List", bg= "#008080", font = ("Times", 11), command = searchList)
    B3W3.grid(column = 0, row = 6)

    B4W3 = Button(text = "Plot List", bg= "#006666", font = ("Times", 11), command = plotList)
    B4W3.grid(column = 0, row = 7)

    B5W3 = Button(text = "Clear List", bg= "#006666", font = ("Times", 11), command = clearList)
    B5W3.grid(column = 0, row = 8)

    Bclear3 = Button(text = "Main Menu", bg = "#ccece6", font = ("Times", 11), command = mainMenu)
    Bclear3.grid(column = 3, row = 1)
    
if __name__ == "__main__":
    mainMenu()
    top.mainloop()

