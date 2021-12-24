"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["cellsize"]=data["boardsize"]/data["rows"] #50 
    data["user"]=emptyGrid(data["rows"],data["cols"])
    data["cp"]=emptyGrid(data["rows"],data["cols"])
    addShips(data["cp"],5)
    data["noofships"]=5
    #data["user"]=createShip()
    #data["cp"]=createShip()
    data["tempship"]=[]
    data["userships"]=0
    data["winner"]=None
    data["maxturns"] =50
    data["currentturn"]=0 
    return data 


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user"],True)
    drawGrid(data, compCanvas,data["cp"],True)
    drawShip(data,userCanvas,data["tempship"])
    drawGameOver(data,userCanvas)
    return

    




'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym=="Return":
        makeModel(data)
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    row,col=getClickedCell(data, event)
    if data["winner"]==None:
     if board=="user":
        clickUserBoard(data,row,col)
    
     if board=="comp":
        runGameTurn(data,row,col)
    
    pass 

     

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    mat=[]
    for i in range(rows):
        x =[]
        for j in range(cols):
            x.append(EMPTY_UNCLICKED)
        mat.append(x)
    return mat
     



'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    r= random.randint(1,8)
    c= random.randint(1,8)
    z= random.randint(0,1)
    if z==0:
        ship=[[r-1,c],[r,c],[r+1,c]]
    else:
        ship=[[r,c-1],[r,c],[r,c+1]]
    
    return ship 
'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in ship:
        for j in i:
            if grid [i[0]][i[1]] !=1:
                return False 
    return True 
   
    return


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    s=0 
    while s < numShips:
        create02= createShip()
        check02= checkShip(grid,create02)
        if check02== True:
            for a in create02:
                grid[a[0]][a[1]]=2
            s+=1
    return grid 
    return


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
  for r in range(data["rows"]):
        for c in range(data["cols"]):
            if grid[r][c]==SHIP_UNCLICKED:
                if showShips==True:
                  canvas.create_rectangle(c*data["cellsize"],r*data["cellsize"],data["cellsize"]+c*data["cellsize"],r*data["cellsize"]+data["cellsize"],fill="yellow")
                else:
                    canvas.create_rectangle(c*data["cellsize"],r*data["cellsize"],data["cellsize"]+c*data["cellsize"],r*data["cellsize"]+data["cellsize"],fill="blue")
            elif grid[r][c]==SHIP_CLICKED:
                canvas.create_rectangle(c*data["cellsize"],r*data["cellsize"],data["cellsize"]+c*data["cellsize"],r*data["cellsize"]+data["cellsize"],fill="red")
            elif grid[r][c]==EMPTY_CLICKED:
                canvas.create_rectangle(c*data["cellsize"],r*data["cellsize"],data["cellsize"]+c*data["cellsize"],r*data["cellsize"]+data["cellsize"],fill="white")
            else:
                canvas.create_rectangle(c*data["cellsize"],r*data["cellsize"],data["cellsize"]+c*data["cellsize"],r*data["cellsize"]+data["cellsize"],fill="blue")
  return 
        


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    z=0
    if ship[z][1]==ship[z+1][1]==ship[z+2][1]:
        ship.sort()
        if ship[z+1][0]-ship[z][0]==1 and ship[z+2][0]-ship[z+1][0]==1:
          return True 
    return False 


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    z=0
    if ship[z][0]==ship[z+1][0]==ship[z+2][0]:
        ship.sort()
        if ship[z+1][1]-ship[z][1]==1 and ship[z+2][1]-ship[z+1][1]==1:
            return True 
    
    return False 

'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    c=data["cellsize"]
    data=[int(event.y/c),int(event.x/c)]
    return data 



'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
   for i in ship:
       r=i[0]
       c=i[1]
       canvas.create_rectangle(c*data["cellsize"],r*data["cellsize"],data["cellsize"]+c*data["cellsize"],r*data["cellsize"]+data["cellsize"],fill="white")
   return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship)==3 and checkShip(grid,ship)==True:
      if (isVertical(ship) or isHorizontal(ship)):
        return True

    return False 


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    r=data["user"]
    if shipIsValid(r, data["tempship"]):
        for i in data["tempship"]:
            r[i[0]][i[1]]=SHIP_UNCLICKED
        data["userships"]=data["userships"]+1
    else:
        print("Ship is not Valid")
    data["tempship"]=[]
    return
    
 


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    r=data["user"]
    if [row,col] in r or data["userships"]==5:
        return
    data["tempship"].append([row,col])
    if len(data["tempship"])==3:
        placeShip(data)
    if data["userships"]==5:
        print("You can start the game")
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col]==SHIP_UNCLICKED:
        board [row][col]=SHIP_CLICKED
    elif board[row][col]==EMPTY_UNCLICKED:
        board[row][col]=EMPTY_CLICKED 
    if isGameOver(board)==True:
        data["winner"]=player    
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    q=data["cp"]
    p=data["user"]
    if q[row][col]==SHIP_CLICKED or q[row][col]==EMPTY_CLICKED:
        return
    else:
        updateBoard(data, q, row, col, "user")
    r,c = getComputerGuess(p)
    updateBoard(data,p,row,col,"comp")
    data["currentturn"]+=1
    if data["currentturn"]==data["maxturns"]:
        data["winner"]="draw"   
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    x=0
    while x!=1:
        r= random.randint(0,9)
        c= random.randint(0,9)
        print(r,c)
        print(len(board[0]),len(board))
        if board[r][c]==SHIP_UNCLICKED or board[r][c]==EMPTY_UNCLICKED:
            return [r,c]
    return 


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range(len(board)):
        if SHIP_UNCLICKED in board[i]:
            return False

    return True 


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
     if data["winner"]=="user":
        canvas.create_text(200, 200, text="Congratulations", font=('Arial',30,'bold italic'), anchor="center")
        canvas.create_text(300, 300, text="Enter to restart game", font=('Arial',25,'bold italic'), anchor="center")
     elif data["winner"]=="comp":
        canvas.create_text(200, 200, text="User Lost", font=('Arial',30,'bold italic'),anchor="center")
        canvas.create_text(300, 300, text="Enter to restart game", font=('Arial',25,'bold italic'), anchor="center")
     elif data["winner"]=="draw":
        canvas.create_text(200, 200, text="Out of moves and reached Draw", font=('Arial',18,'bold italic'),anchor="center") 
        canvas.create_text(300, 300, text="Enter to restart game", font=('Arial',25,'bold italic'), anchor="center")  
     
     return 




### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop() 


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    
