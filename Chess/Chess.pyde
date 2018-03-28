#Import other classes and declare global variables
import GameState as gs
from Tile import Tile
#Create begining game board
gameState = gs.newGame()

def setup():
    size(1000,800)
    textAlign(CENTER)
    rectMode(CENTER)

def draw():
    background(150)
    gs.interfaceUpdate()
    #Use the global gameState variable
    global gameState
    #Display all items in gameState
    grey = True
    for x in range(8):
        grey = not grey
        for y in range(8):
            grey = not grey
            gameState[x][y].display(grey)

def mouseClicked():
    #Use the global gameState variable
    global gameState
    #Buttons
    x = int((mouseX)/100)
    y = int((mouseY)/100)
    if x < 8 and y < 8:
        gameState[x][y].clicked(gameState)
